import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
import json
from flask import current_app,g

class DB():
    engine = None
    session = None

    def __init__(self, new_engine):
        self.engine = new_engine
        self.session = sessionmaker(bind=self.engine)()

    def select_fetch_all(self, sql):
        result = self.engine.execute(sql)
        keys = result.keys()
        rows = result.fetchall()
        output = []
        for r in rows:
            output_row = {}
            for i in range(len(keys)):
                output_row[keys[i]] = r[i]
            output.append(output_row)
        return output


def init_db():
    config = current_app.config
    
    hostname = config['MYSQL_HOSTNAME']
    username = config['MYSQL_USERNAME']
    password = config['MYSQL_PASSWORD']
    port     = config['MYSQL_PORT']
    schema   = config['MYSQL_SCHEMA']
    
    jakmap_engine = sqlalchemy.create_engine('mysql+mysqldb://'+username+':'+password+'@'+hostname+':'+port+'/'+schema, pool_recycle=600)
    
    g.dbs = {}
    g.dbs['jakmap'] = DB(jakmap_engine)
    g.foo = 'bar'
