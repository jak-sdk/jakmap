from .jmap import JMAP
from definitions import *
from flask import current_app, g


class Email:
    
    # metadata
    email_id = None
    blob_id = None
    thread_id = None
    mailbox_ids = None
    keywords = None
    size = None
    received_at = None
    
    #header fields
    raw = None
    text = None
    addresses = None # EmailAddress class
    grouped_addresses = None # EmailAddressGroup class
    message_ids = None
    date = None
    urls = None

    #lower level
    headers = None # EmailHeader class

    # convenience
    message_id = None
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


