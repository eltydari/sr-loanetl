# -- FILE: loan_etl/db/schema/base.py
'''
Base table schema
'''
import re
from   sqlalchemy.ext.declarative import declarative_base

MODE_INSERT = 0
MODE_UPDATE = 1
PAT_NAME = re.compile("[._a-zA-Z]*table_([a-zA-Z]+)")

BaseTable = declarative_base()