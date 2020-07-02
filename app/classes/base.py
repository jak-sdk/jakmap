class Base:
    # weird territory here, semi abstract base class that gets overridden later..?

    client_properties = []
    server_properties = []

    @property
    def properties(self):
        return client_properties + server_properties

    def __init__(self):
       pass 

    @classmethod
    def create(cls, tempId, obj):
        obj = cls().patch(obj).save()
        return obj

    def patch(self, patchObject):
        if patchObject:
            for prop, value in patchObject.properties:
                if prop in self.client_properties:
                    self.setattr(prop, value)
                else:
                    #return invalid parameter
                    pass

    @JMAP.abstract
    @classmethod
    def loadById(cls, Id):
        pass

    
    @classmethod
    def load(cls, Id):
        return cls.loadbyId(Id)

    @JMAP.abstract
    def save(self):
        pass
