from .jmap import JMAP
from definitions import *

class Mailbox:
    
    @JMAP.registerMethodAs("Mailbox/get", CAP_MAIL)
    def getMailbox(args, methodcallid):
        print("mailbox :)")
        return args
