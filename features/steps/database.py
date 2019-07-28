# -- FILE: features/steps/database.py
import loan_etl.db.loader as dbimpl
import pandas as pd
import sqlalchemy as dbapi

def setupTable(context, tableName):
    schema = dbapi.MetaData()
    columns = [dbapi.Column(header, dbapi.String()) 
                for header in context.table.headings]
    dbapi.Table(tableName, schema, *columns)
    context.db.setupTables(schema = schema)

@given(u"a database")
def given_database(context):
    context.db = dbimpl.DbLoader()

@when(u"I load a table named \"{tableName}\" with the following")
def when_load_table(context, tableName):
    setupTable(context, tableName)
    df = pd.DataFrame(columns = context.table.headings)
    for row in context.table.rows:
        pdrow = dict(zip(context.table.headings, row))
        df = df.append(pdrow, ignore_index=True)
    context.db.load(df)

@when(u"I query the database with \"{query}\"")
def when_query_table(context, query):
    connection = context.db._engine.connect()
    context.result = pd.DataFrame(connection.execute(query).fetchall())