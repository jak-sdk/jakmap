from .jmap import JMAP
from definitions import *
from flask import current_app, g


class SearchSnippet:
    
    @JMAP.registerMethodAs("SearchSnippet/get", CAP_MAIL)
    def get(args, methodcallid):
        print("mailbox :)")
        return args

