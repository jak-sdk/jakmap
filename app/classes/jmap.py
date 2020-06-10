import functools
from flask import current_app, g
from helpers import *

# a messy class to handle pulling apart the request
# calling all the methods
# and aggregating the results
class JMAP:
    _JMAPMethods = {}

    @property 
    def Methods(self):
        return type(self)._JMAPMethods

    @classmethod
    def process(cls, request):
        # housekeeping
        #   check capabilities

        dprint(str(request))
        
        # meat of the method
        method_call_responses = []
        for i in request['methodCalls']:
            methodname   = i[0]
            args         = i[1]
            methodcallid = i[2]
            #methodnames object/method -> object.method
            if methodname in cls._JMAPMethods:
                dprint(methodname + "exists, calling " + str(cls._JMAPMethods[methodname]['method']))
                
                # part of spec, 
                # a method can respond with multiple responses
                # and it is the callid that ids these, not the methodname
                method_responses = cls._JMAPMethods[methodname]['method'](args, methodcallid)
                #NOTSPEC
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

        return response

    @classmethod 
    def registerMethodAs(cls, MethodName, capName):
        # this 'injects' the MethodName into the decorator 
        def register(func):
            # put in globals
            cls._JMAPMethods[MethodName]  = {}
            cls._JMAPMethods[MethodName]['method']  = func
            cls._JMAPMethods[MethodName]['capName'] = capName
            dprint("registering " + MethodName + " under " + capName)
            return func
            
        return register

            
