

class User(object):
    username = "fooname"

    def get_accounts(self):
        output = {
          "A13824": {
            "name": "john@example.com",
            "isPersonal": True,
            "isReadOnly": False,
            "accountCapabilities": {
              "urn:ietf:params:jmap:mail": {
                "maxMailboxesPerEmail": None,
                "maxMailboxDepth": 10
              },
              "urn:ietf:params:jmap:contacts": {
                "foobar": None,
              }
            }
          }
        }
        return output

    def get_primary_accounts(self):
        output = {
          "urn:ietf:params:jmap:mail": "A13824",
          "urn:ietf:params:jmap:contacts": "A13824"
        }
        return output
