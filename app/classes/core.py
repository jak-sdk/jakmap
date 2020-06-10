from .jmap import JMAP
from definitions import *

class Core:
    
    @JMAP.registerMethodAs("Core/echo", CAP_CORE)
    def getMailbox(args, methodcallid):
        return [args]
