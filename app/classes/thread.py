from .jmap import JMAP
from definitions import *
from flask import current_app, g


class Thread:
    
    thread_id = None
    email_ids = []


    @JMAP.registerMethodAs("Thread/get", CAP_MAIL)
    def get(args, methodcallid):
        print("Thread :)")
        return args

    @JMAP.registerMethodAs("Thread/changes", CAP_MAIL)
    def changes(args, methodcallid):
        print("Thread :)")
        return args


