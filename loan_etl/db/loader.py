# -- FILE: src/loan_etl/db/loader.py
'''
Handles loading of data into SQL database
'''
import sqlalchemy as db

class DbLoader(object):

    def __init__(self, dbtype="sqlite", dbloc="/:memory:", username="", password=""):
        accessFields = ""
        if username and password:
            accessFields = ':'.join(username, password) + '@'
        self._engine = db.create_engine("{}://{}{}".format(dbtype, accessFields, dbloc))
        self.connection = self._engine.connect()
        
    def load(self):
        pass 