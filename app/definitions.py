CAP_CORE     = "urn:ietf:params:jmap:core"
CAP_MAIL     = "urn:ietf:params:jmap:mail"
CAP_CONTACTS = "urn:ietf:params:jmap:contacts"

# these probably shouldn't be here
INVALID_JSON = '''{
  "type": "urn:ietf:params:jmap:error:notJSON",
  "status": 400,
  "detail": "The content type of the request was not application/json or the request did not parse as I-JSON."
}'''

UNKNOWN_CAPABILITY= '''{
  "type": "urn:ietf:params:jmap:error:unknownCapability",
  "status": 400,
  "detail": "The client included a capability in the “using” property of the request that the server does not support."
}'''

SERVER_IMPLEMENTATION_ERROR= '''{
  "type": "urn:ietf:params:jmap:error:badImplementation",
  "status": 500,
  "detail": "This server has not implemented a method that this request depends on. Please email the administrators expressing your dissapointment."
}'''
