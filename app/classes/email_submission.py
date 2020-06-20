from .jmap import JMAP
from definitions import *
from flask import current_app, g


class EmailSubmission:
    
    email_submission_id = None
    identity_id= None
    email_id = None
    thread_id = None
    envelope = None # Envelope
    send_at = None
    undo_status = None
    delivery_status = None # DeliveryStatus
    delivered = None
    displayed = None
    dsn_blob_ids = None
    mdn_blob_ids = None
     = None


    @JMAP.registerMethodAs("EmailSubmission/get", CAP_MAIL)
    def get(args, methodcallid):
        print("EmailSubmission :)")
        return args

    @JMAP.registerMethodAs("EmailSubmission/set", CAP_MAIL)
    def set(args, methodcallid):
        print("EmailSubmission :)")
        return args

    @JMAP.registerMethodAs("EmailSubmission/changes", CAP_MAIL)
    def changes(args, methodcallid):
        print("EmailSubmission :)")
        return args

    @JMAP.registerMethodAs("EmailSubmission/query", CAP_MAIL)
    def query(args, methodcallid):
        print("EmailSubmission :)")
        return args

    @JMAP.registerMethodAs("EmailSubmission/queryChanges", CAP_MAIL)
    def queryChanges(args, methodcallid):
        print("EmailSubmission :)")
        return args


