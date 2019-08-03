# -- FILE: loan_etl/db/loader.py
'''
Handles loading of data into SQL database
'''
import sqlalchemy as db
from   .schema import get_schema

SCHEMA = get_schema()

class DbLoader(object):

    def __init__(self, dbtype="sqlite", dbloc="/:memory:", username="", password=""):
        accessFields = ""
        if username and password:
            accessFields = ':'.join(username, password) + '@'
        self._engine = db.create_engine("{}://{}{}".format(dbtype, accessFields, dbloc))
        self._conn = self._engine.connect()

    def setupTables(self, schema=SCHEMA):
        self._schema = schema
        self._schema.create_all(self._engine)
        
    def load(self, df_data, mapper={}):
        # Note: df_data needs to be a pandas dataframe
        if not mapper:
            table = self._schema.tables[list(self._schema.tables.keys())[0]]
            data = [dict(row) for _, row in df_data.iterrows()]
            return self._conn.execute(db.insert(table), data)
        tables = {}
        for _, row in df_data.iterrows():
            entry = {}
            for k,v in row.items():
                destinations = mapper[k]["destination"]
                for destination in destinations:
                    entry.setdefault(destination,{})[k] = v
            for dest, drow in entry.items():
                tables.setdefault(dest, []).append(drow)
        return tuple(self._conn.execute(db.insert(self._schema.tables[tableName]), data) 
                        for tableName, data in tables.items())

