from .jmap import JMAP
from definitions import *
from flask import current_app, g


class Mailbox:
    
    mailbox_id = None
    name = None
    parent_id = None
    role = None
    sort_order = None
    total_emails = None
    unread_emails = None
    total_threads = None
    unread_threads = None
    my_rights = None # MailboxRights class
    is_subscribed = None


    @JMAP.registerMethodAs("Mailbox/get", CAP_MAIL)
    def get(args, methodcallid):
        response = {}
        response['accountId'] = args['accountId']
        response['state'] = '123'
        response['list'] = []
        response['notFound'] = []
        # if len(args['ids']) > 1000?:
        #  return requestTooLarge
        return response

    @JMAP.registerMethodAs("Mailbox/set", CAP_MAIL)
    def set(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/changes", CAP_MAIL)
    def changes(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/query", CAP_MAIL)
    def query(args, methodcallid):
        print("mailbox :)")
        # FilterCondition class
        return args

    @JMAP.registerMethodAs("Mailbox/queryChanges", CAP_MAIL)
    def queryChanges(args, methodcallid):
        print("mailbox :)")
        return args


