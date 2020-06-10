CAP_CORE     = "urn:ietf:params:jmap:core"
CAP_MAIL     = "urn:ietf:params:jmap:mail"
CAP_CONTACTS = "urn:ietf:params:jmap:contacts"

INVALID_JSON = '''{
  "type": "urn:ietf:params:jmap:error:notJSON",
  "status": 400,
  "detail": "The content type of the request was not application/json or the request did not parse as I-JSON."
}'''
