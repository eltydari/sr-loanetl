# -- FILE: src/loan_etl/db/loader.py
import sqlalchemy as orm

class DbLoader(object):

    def __init__(self, dbtype, usrname, passwd, dbloc):
        self._engine = orm.create_engine("{}://{}:{}@{}".format(dbtype, usrname, passwd, dbloc))
        self.connection = self._engine.connect()
        
    def load(self):
        pass