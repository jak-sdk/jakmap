from _db import dbs
from sqlalchemy.ext.declarative import declarative_base
import json

class Base(object):
    db = dbs['jakmap']

    def save(self):
        self.db.session.add(self)
        self.db.session.commit()

    @classmethod
    def load(cls, id):
        obj = cls.db.session.query(cls).filter(cls.__mapper__.primary_key[0] == id).first()
        return obj

    @classmethod
    def load_by_name(cls, name):
        obj = cls.db.session.query(cls).filter(cls.name == name).first()
        return obj

    @classmethod
    def listable_fields(cls):
        # default to all defined columns
        # please override this function when desireable
        # e.g. you want to hide certain columns from a default web view
        return cls.__table__.columns

    def json(self):
        json_array = {}
        for column in self.__class__.__table__.columns:
            json_array[column.name] = getattr(self,column.name)
        return json.dumps(json_array, indent=2)

    def json_listable_fields(self):
        json_array = {}
        for column in self.listable_fields():
            json_array[column.name] = getattr(self,column.name)
        return json.dumps(json_array, indent=2)

    def array_listable_fields(self):
        output = {}
        for column in self.listable_fields():
            output[column.name] = getattr(self,column.name)
        return output


    @classmethod
    def all(cls): 
        obj_array = cls.db.session.query(cls).all() 
        return obj_array

Base = declarative_base(cls=Base)
