from hashlib import sha256
import json
from flask import current_app, g

def session_resource():
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

    output['capabilities'] = {}
    output['capabilities']['urn:ietf:params:jmap:core'] = core
    output['capabilities']["urn:ietf:params:jmap:mail"] = {}
    output['capabilities']["urn:ietf:params:jmap:contacts"] = {}
   
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
