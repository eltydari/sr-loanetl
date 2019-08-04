# -- FILE: loan_etl/db/loader.py
'''
Handles loading of data into SQL database
'''
import sqlalchemy as db

class DBLoader(object):

    def __init__(self, dbtype="sqlite", url="", username="", password=""):
        accessFields = ""
        if username and password:
            accessFields = ':'.join(username, password) + '@'
        self._engine = db.create_engine("{}://{}{}".format(dbtype, accessFields, url))
        self._conn = self._engine.connect()

    def setupTables(self, schema):
        self._schema = schema
        self._schema.create_all(self._engine)
        
    def load(self, df_data, mapping={}):
        # Note: df_data needs to be a pandas dataframe
        if not hasattr(self, "_schema"):
            raise Exception("Database loader does not have tables setup. \
                             Call setupTables method with a valid schema.")
        if not mapping:
            table = self._schema.tables[list(self._schema.tables.keys())[0]]
            data = [dict(row) for _, row in df_data.iterrows()]
            return self._conn.execute(db.insert(table), data)
        tables = {}
        for _, row in df_data.iterrows():
            entry = {}
            for k,v in row.items():
                destinations = mapping[k]["destTables"]
                for destination in destinations:
                    entry.setdefault(destination,{})[k] = v
            for dest, drow in entry.items():
                tables.setdefault(dest, []).append(drow)
        return tuple(self._conn.execute(db.insert(self._schema.tables[tableName]), data) 
                        for tableName, data in tables.items())

