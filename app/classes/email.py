from .jmap import JMAP
from definitions import *
from flask import current_app, g
import email


class Email:
    
    # metadata
    email_id = None
    blob_id = None
    thread_id = None
    
    @property
    def mailboxIds(self):
        # weird format https://jmap.io/spec-mail.html#properties-of-the-email-object
        #{'1':True,'3':True}
        ret = {}
        for m in self.mailboxes():
            ret[m.mailboxId] = True
        return ret

    @property
    def keywords(self):
        return {
            '$draft': self.isDraft,
            '$seen': self.isSeen,
            '$flagged': self.isFlagged,
            '$answered': self.isAnswered
            #todo custom keywords
        }

    @property
    def size(self):
        #todo
        #return self.size
        pass

    @property
    def receivedAt(self):
        #todo
        #return self.receivedAt
        pass
    
    @property
    def headers(self):
        #todo get all headers
        pass

    def getHeader(self, name, headerForm=None, allInstances=False):
        #todo get specific header
        pass
    

    raw = None
    text = None
    addresses = None # EmailAddress class
    grouped_addresses = None # EmailAddressGroup class
    message_ids = None
    date = None
    urls = None

    convenienceProperties = {
        'messageId' : 'header:Message-ID:asMessageIds',
        'inReplyTo' : 'header:In-Reply-To:asMessageIds',
        'references' : 'header:References:asMessageIds',
        'sender' : 'header:Sender:asAddresses',
        'from' : 'header:From:asAddresses',
        'to' : 'header:To:asAddresses',
        'cc' : 'header:Cc:asAddresses',
        'bcc' : 'header:Bcc:asAddresses',
        'replyTo' : 'header:Reply-To:asAddresses',
        'subject' : 'header:Subject:asText',
        'sentAt' : 'header:Date:asDate'
    }
    # We want the above as properties for sake of convenience
    # this code generates them in the form:
    # @property
    # def messageId(self):
    #     return self.getHeaderByLongName('header:Message-ID:asMessageIds')
    for k,v in convenienceProperties.items():
        def __f(a):
            return lambda self : self.getHeaderByLongName(a)
        vars()[k] = property(__f(v))
    del k,v,__f

    def getHeaderByLongName(self, header):
        hsplit = header.split(":")
        #todo hsplit[2] == asBlahBlah
        #todo check hsplit[0] == header
        #call getHeader(hsplit[1], asBlahBlah
        pass
    
    in_reply_to = None
    references = None
    sender = None
    #from = None
    to = None
    cc = None
    bcc = None
    reply_to = None
    subject = None
    sent_at = None

    # body parts
    # EmailBodyPart class
    emailBodyParts = None # todo in backend sqlalchemy relationship?
    part_id = None
    blob_id = None
    size = None
    headers = None
    name  = None
    #type = None
    charset = None
    disposition = None
    cid = None
    language = None
    sub_parts = None
    
    #
    body_structure = None # EmailBodyPart class
    body_values = None # EmailBodyValue class
    text_body = None
    html_body = None
    attachments = None
    has_attachment = None
    preview = None

    @JMAP.registerMethodAs("Mailbox/get", CAP_MAIL)
    def get(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/set", CAP_MAIL)
    def set(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/copy", CAP_MAIL)
    def copy(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/import", CAP_MAIL)
    def import(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/parse", CAP_MAIL)
    def parse(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/changes", CAP_MAIL)
    def changes(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/query", CAP_MAIL)
    def query(args, methodcallid):
        print("mailbox :)")
        return args

    @JMAP.registerMethodAs("Mailbox/queryChanges", CAP_MAIL)
    def queryChanges(args, methodcallid):
        print("mailbox :)")
        return args


