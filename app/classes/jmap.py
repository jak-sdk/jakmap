import functools
from flask import current_app, g
from helpers import *
from .result_reference import ResultReference

# a messy class to handle pulling apart the request
# calling all the methods
# and aggregating the results
class JMAP:
    _JMAPMethods     = dict()
    _JMAPCaps        = set()

    @property 
    def Methods(self):
        return type(self)._JMAPMethods

    @property 
    def Caps(self):
        return type(self)._JMAPCaps

    @classmethod
    def process(cls, request):
        # housekeeping
        #   check capabilities
        for cap in request['using']:
            if cap not in cls._JMAPCaps:
                raise UnknownCapability()

        #dprint(str(request))

        #check type signature
        
        # meat of the method
        method_call_responses = []
        for i in request['methodCalls']:
            methodname   = i[0]
            args         = i[1]
            methodcallid = i[2]
            #methodnames object/method -> object.method
            if methodname in cls._JMAPMethods:
                dprint(methodname + "exists, calling " + str(cls._JMAPMethods[methodname]['method']))

                for k in [_k for _k in args.keys() if _k[0] == '#']:
                  try:
                    resultReference = ResultReference(args[k]['resultOf'], args[k]['name'],args[k]['path'])
                    args[k.strip("#")] = JMAP.findResultIn(resultReference, method_call_responses)
                  except:
                    #invalid reference
                    pass
                
                # a method can respond with multiple responses
                # and it is the callid that ids these, not the methodname
                method_responses = cls._JMAPMethods[methodname]['method'](args, methodcallid)

                # we may need to allow a method to call another method, and this would
                # add two entries to method_call_responses with the same methodcallid
                for mr in method_responses:
                    method_call_responses.append([
                        methodname,
                        mr,
                        methodcallid
                    ])
            else:
                method_call_responses.append([
                    "error",
                    {"type" : "unknownMethod"},
                    methodcallid
                ])
        
        response = {}
        response['methodResponses']  = method_call_responses
        response['sessionState'] = cls.sessionState()

        return response

    @classmethod 
    def registerMethodAs(cls, MethodName, capName):
        # this 'injects' the MethodName into the decorator 
        def register(func):
            @functools.wraps(func)
            def newfunc(*args, **kwargs):
                output = func(*args, **kwargs)
                return output

            # put in globals
            cls._JMAPMethods[MethodName]  = {}
            cls._JMAPMethods[MethodName]['method']  = newfunc
            cls._JMAPMethods[MethodName]['capName'] = capName
            cls._JMAPCaps.add(capName)
            dprint("registering " + MethodName + " under " + capName)

            return newfunc
            
        return register

    @classmethod
    def sessionState(cls):
        return "abcdef123456"

    @classmethod
    def getPreviousResult(cls, resultReference):
        # this f finds a previous result based on the passed in ResultReference
        pass

    @classmethod
    def sessionResource(cls):
        config = current_app.config
        output = {}

        #get capabilities
        core = {}
        core["maxSizeUpload"] = config['MAXSIZEUPLOAD']
        core["maxConcurrentUpload"] = config['MAXCONCURRENTUPLOAD']
        core["maxSizeRequest"] = config['MAXSIZEREQUEST']
        core["maxConcurrentRequests"] = config['MAXCONCURRENTREQUESTS']
        core["maxCallsInRequest"] = config['MAXCALLSINREQUEST']
        core["maxObjectsInGet"] = config['MAXOBJECTSINGET']
        core["maxObjectsInSet"] = config['MAXOBJECTSINSET']
        core["collationAlgorithms"] = [
          "i;ascii-numeric",
          "i;ascii-casemap",
          "i;unicode-casemap"
        ]

        # is this account based? Do we use what's registered in JMAP?
        output['capabilities'] = {}
        output['capabilities']['urn:ietf:params:jmap:core'] = core

        # for now, offer all JMAP Caps, in future, we can restrict certain accounts
        # for cap in g.user.allowedCaps:
        for cap in JMAP.Caps:
            output['capabilities'][cap] = {}

        #get accounts
        output['accounts'] = g.user.get_accounts()
        output['primaryAccounts'] = g.user.get_primary_accounts()
        output['username'] = g.user.username
        output['apiUrl'] = config['APIURL']
        output['downloadUrl'] = config['DOWNLOADURL']
        output['uploadUrl'] = config['UPLOADURL']
        output['eventSourceUrl'] = config['EVENTSOURCEURL']
        state = sha256(json.dumps(output).encode('utf-8')).hexdigest()
        output['state'] = state

        return output
            
