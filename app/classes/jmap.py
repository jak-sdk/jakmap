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
        
        # meat of the method
        for i in request['methodCalls']:
            methodname   = i[0]
            args         = i[1]
            methodcallid = i[2]
            #methodnames object/method -> object.method


        return request

    @classmethod 
    def registerMethodAs(cls, MethodName):
        # this 'injects' the MethodName into the decorator 
        def register(func):
            # put in globals
            cls._JMAPMethods[MethodName] = func
            dprint("registering " + MethodName)
            return func
            
        return register

            
