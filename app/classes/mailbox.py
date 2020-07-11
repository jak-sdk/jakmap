from .jmap import JMAP
from .base import Base
from definitions import *
from flask import current_app, g


class Mailbox(Base):
    
    client_properties = [
        'name', 'parent_id', 'role']
    server_properties = [
        'total_emails',
        'unread_emails',
        'total_threads',
        'unread_threads',
        'my_rights', # mailboxrights class
        'is_subscribed']

    filterableConditions = [
        'parentId',   # Id|null The Mailbox parentId property must match the given value exactly.
        'name',       # String The Mailbox name property contains the given string.
        'role',       # String|null The Mailbox role property must match the given value exactly.
        'hasAnyRole', # Boolean If true, a Mailbox matches if it has any non-null value for its role property.
        'isSubscribed'] # Boolean The isSubscribed property of the Mailbox must be identical to the value given to match the condition.


    mailbox_id = None
    account_id = None
    sort_order = None

    @JMAP.registerMethodAs("Mailbox/get", CAP_MAIL)
    def get(args, methodcallid):
        mailboxes = [Mailbox.loadById(Id) for Id in args['ids'] if g.user.canViewMailbox(Id)]

        #todo implement handling of args['properties']

        response = {}
        response['accountId'] = args['accountId']
        response['state'] = Mailbox.state()
        response['list'] = [mailbox.toList() for mailbox in mailboxes]
        response['notFound'] = [Id for Id in args['ids'] if Id not in [MB['id'] for MB in response['list']] ]
        # todo implement requestTooLarge
        # if len(args['ids']) > 1000?:
        #  return requestTooLarge
        return [response]

    @JMAP.registerMethodAs("Mailbox/set", CAP_MAIL)
    def set(args, methodcallid):
        stateMismatch = False
        try:
            if args['ifInState'] != Mailbox.state():
                stateMismatch = True
                pass
            else:
                pass
        except(KeyError):
            # I guess there's no ifInState
            pass

        if stateMismatch:
            # todo response = stateMismatch
            pass
        else:
            for i,obj in args['create']:
                # create obj Foo with temp-id i
                patchObj = PatchObject(obj)
                Mailbox().patch(patchObj).save()

            for i,obj in args['update']:
                # update obj with temp-id i
                patchObj = PatchObject(obj)
                Mailbox.load(i).patch(patchObj).save()

            for i in args['destroy']:
                # destroy obj with temp-id i
                m = Mailbox.load(i)
                if m.hasChild(): #todo
                    pass #todo return mailboxHasChild
                else if m.mailboxHasEmail() and !args['onDestroyRemoveEmails']:
                    pass #todo return m.mailboxHasEmail
                else:
                    m.destroy()

        return args


    @JMAP.registerMethodAs("Mailbox/changes", CAP_MAIL)
    def changes(args, methodcallid):
        # todo assert maxChanges is +int

        # todo what mailbox?
        changes = Mailbox.getChangesSince(args['sinceState'])

        # todo respond cannotCalculateChanges if ..

        response = {}
        response['accountId'] = args['accountId']
        response['oldState'] = args['sinceState']
        response['newState'] = max([change['state'] for change in changes])
        response['hasMoreChanges'] = (args['maxChanges'] < len(changes))
        response['created'] = [change['id'] for change in changes if change['created']]
        response['updated'] = [change['id'] for change in changes if change['updated']]
        response['destroyed'] = [change['id'] for change in changes if change['destroyed']]
        return [response]

    @JMAP.registerMethodAs("Mailbox/query", CAP_MAIL)
    def query(args, methodcallid):
        Id = args['accountId']
        filt = Filter(args['filter'], self.filterableConditions)
        mbs = Mailbox.filter(filt)
        sort = Sort(args['sort'])
        return sort.applyTo(mbs) # todo data format for query

    @JMAP.registerMethodAs("Mailbox/queryChanges", CAP_MAIL)
    def queryChanges(args, methodcallid):
        # todo queryChanges, stop being lazy with cannotCalculateChanges
        # for now, cannotCalculateChanges
        response = {'type': 'cannotCalculateChanges'}
        return [response]

    @classmethod
    def state(cls):
        # https://jmap.io/server.html#algorithms
        return cls.highModSeqMailbox()

    
    ###########
    # Abstracts

    @JMAP.abstract
    @classmethod
    def highModSeqMailbox(cls):
        pass


