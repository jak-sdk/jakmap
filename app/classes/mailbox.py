from .jmap import JMAP

class Mailbox:
    
    @JMAP.registerMethodAs("Mailbox/get")
    def getMailbox(args, methodcallid):
        print("mailbox :)")
        return args
