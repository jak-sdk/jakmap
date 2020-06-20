from .jmap import JMAP
from definitions import *
from flask import current_app, g


class Identity:
    
    identity_id = None
    name = None
    email = None
    reply_to = None
    bcc = None
    text_signature= None
    html_signature= None
    may_delete = None
    = None
    = None
    = None


    @JMAP.registerMethodAs("Identity/get", CAP_MAIL)
    def get(args, methodcallid):
        print("Identity :)")
        return args

    @JMAP.registerMethodAs("Identity/set", CAP_MAIL)
    def set(args, methodcallid):
        print("Identity :)")
        return args

    @JMAP.registerMethodAs("Identity/changes", CAP_MAIL)
    def changes(args, methodcallid):
        print("Identity :)")
        return args

