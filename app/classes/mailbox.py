from .jmap import JMAP

class Mailbox:
    
    @JMAP.registerMethodAs("Mailbox/get")
    def getMailbox():
        print("mailbox :)")
