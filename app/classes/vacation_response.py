from .jmap import JMAP
from definitions import *
from flask import current_app, g


class VacationResponse:
    
    vacation_repsonse_id = None
    is_enabled = None
    from_date = None
    to_date = None
    subject = None
    text_body = None
    html_body = None
     = None
     = None
     = None
     = None


    @JMAP.registerMethodAs("Mailbox/get", CAP_MAIL)
    def get(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/set", CAP_MAIL)
    def set(args, methodcallid):
        print("mailbox :)")
        return args

