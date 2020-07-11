from .jmap import JMAP
from definitions import *
from flask import current_app, g


class Thread:
    
    thread_id = None
    email_id = None
    email_ids = []

    @JMAP.registerMethodAs("Thread/get", CAP_MAIL)
    def get(args, methodcallid):
        emailList = []
        for thread_id in args['ids']:
            emailList.append({ 
                'id':thread_id,
                'emailIds':Email.getByThreadId(thread_id)})
        response = {}
        response['accountId'] = args['accoundId']
        response['state'] = 
        return args

    @JMAP.registerMethodAs("Thread/changes", CAP_MAIL)
    def changes(args, methodcallid):
        print("Thread :)")
        return args


