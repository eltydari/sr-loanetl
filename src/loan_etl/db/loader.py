# -- FILE: src/loan_etl/db/loader.py
import sqlalchemy as db

class DbLoader(object):

    def __init__(self, dbtype, usrname, passwd, dbloc):
        self._engine = db.create_engine("{}://{}:{}@{}".format(dbtype, usrname, passwd, dbloc))
        self.connection = self._engine.connect()
        
    def load(self):
        pass