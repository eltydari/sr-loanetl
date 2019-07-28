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

    def setupTables(self, schema):
        self._schema = schema
        self._schema.create_all(self._engine)
        
    def load(self, df_data, configuration={}):
        # Note: df_data needs to be a pandas dataframe
        if not configuration:
            tableName = self._schema.tables[list(self._schema.tables.keys())[0]]
            data = [dict(row) for _, row in df_data.iterrows()]
            return self._conn.execute(db.insert(tableName), data)
        pass