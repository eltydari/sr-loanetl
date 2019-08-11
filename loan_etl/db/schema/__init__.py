# -- FILE: loan_etl/db/schema/__init__.py
from .base import MODE_INSERT, MODE_UPDATE

def getSchema(*args):
    from   collections import namedtuple
    import importlib
    import importlib.util
    Schema = namedtuple('Schema', ['metadata', 'tables'])

    tables = {}
    for tableName in args:
        modname = "{}.table_{}".format(__name__, tableName)
        if not importlib.util.find_spec(modname):
            raise KeyError("Table schema \"{}\" not found.".format(modname))
        tables[tableName] = getattr(importlib.import_module(modname), tableName.capitalize())
    baseclass = importlib.import_module("{}.{}".format(__name__, "base"))
    return Schema(getattr(baseclass, "BaseTable").metadata, tables)