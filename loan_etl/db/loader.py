# -- FILE: loan_etl/db/loader.py
'''
Handles loading of data into SQL database
'''
from   ..validators.datatype import ERROR
import sqlalchemy as db
from   sqlalchemy.orm import sessionmaker

class DBLoader(object):

    def __init__(self, dbtype="sqlite", url="", username="", password="", debug=False):
        accessFields = ""
        if username and password:
            accessFields = ':'.join([username, password]) + '@'
        self._engine = db.create_engine("{}://{}{}".format(dbtype, accessFields, url), echo=debug)
        self._session = sessionmaker()
        self._session.configure(bind=self._engine)

    def setupTables(self, schema):
        self._schema = schema
        self._schema.create_all(self._engine)
        
    def load(self, df_data, mapping={}):
        # Note: df_data needs to be a pandas dataframe
        if not mapping:
            table = self._schema.tables[list(self._schema.tables.keys())[0]]
            data = [dict(row) for _, row in df_data.iterrows()]
            return self._engine.connect().execute(db.insert(table), data)

        tables = self._preprocessLoad(df_data, mapping)

        if not hasattr(self, "_schema"):
            from .schema import getSchema, MODE_INSERT, MODE_UPDATE
            schema, tableClasses = getSchema(*tables.keys())
            self.setupTables(schema)
            for tableName, data in tables.items():
                cSession = self._session()
                #try:
                tableClass = tableClasses[tableName]
                for row in data:
                    dataRow = tableClass(**row)
                    if dataRow.mode == MODE_INSERT:
                        cSession.add(dataRow)
                    elif dataRow.mode == MODE_UPDATE:
                        cSession.merge(dataRow)
                cSession.commit()
                cSession.close()
                #finally:
                #    cSession.close()
            return

        return tuple(self._engine.connect().execute(db.insert(self._schema.tables[tableName]), data) 
                        for tableName, data in tables.items())

    def _preprocessLoad(self, df_data, mapping):
        tables = {}
        for _, row in df_data.iterrows():
            entry = {}
            for k,v in row.items():
                if k == ERROR:
                    destinations = ["logs"]
                else:
                    destinations = mapping[k]["destTables"]
                for destination in destinations:
                    entry.setdefault(destination,{})[k] = v
            for dest, drow in entry.items():
                tables.setdefault(dest, []).append(drow)
        return tables

