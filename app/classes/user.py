from .jmap import JMAP

class User(object):
    username = None

    @JMAP.abstract
    def get_accounts(self):
        pass

    @JMAP.abstract
    def get_primary_accounts(self):
        pass

    @JMAP.abstract
    def canViewMailbox(self, Id):
        pass
        # return self.canViewAccount(Mailbox.account)

    @JMAP.abstract
    def canViewAccount(self, Id):
        pass
        #return exists(user__account)
