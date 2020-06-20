from definitions import *

class JakmapException(Exception):
    status_code = None
    message = None

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv

class InvalidJSON(JakmapException):
    status_code = 400
    message = INVALID_JSON

class UnknownCapability(JakmapException):
    status_code = 400
    message = UNKNOWN_CAPABILITY

class AbstractMethodCalled(JakmapException):
    status_code = 500
    message = SERVER_IMPLEMENTATION_ERROR
