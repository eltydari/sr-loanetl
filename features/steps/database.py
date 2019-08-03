# -- FILE: features/steps/database.py
import loan_etl.db.loader as dbimpl
import pandas as pd
import sqlalchemy as dbapi

@given(u"a database")
def given_database(context):
    context.db = dbimpl.DbLoader()

@given(u"I have a table named \"{tableName}\" with the following headers")
def given_table_schema(context, tableName):
    if not hasattr(context, "schema"):
        context.schema = dbapi.MetaData()
    headers = context.text.split('\n')
    columns = [dbapi.Column(header, dbapi.String()) 
                for header in headers]
    dbapi.Table(tableName, context.schema, *columns)
    context.db.setupTables(schema = context.schema)

@step(u"I load the following into the database")
def step_load_table(context):
    df = pd.DataFrame(columns = context.table.headings)
    for row in context.table.rows:
        pdrow = dict(zip(context.table.headings, row))
        df = df.append(pdrow, ignore_index=True)
    context.db.load(df)

@step(u"I load, using the configuration, the following into the database")
def step_config_load_table(context):
    df = pd.DataFrame(columns = context.table.headings)
    for row in context.table.rows:
        pdrow = dict(zip(context.table.headings, row))
        df = df.append(pdrow, ignore_index=True)
    context.db.load(df, mapper=context.cfg)

@when(u"I query the database with \"{query}\"")
def when_query_table(context, query):
    connection = context.db._engine.connect()
    context.result = pd.DataFrame(connection.execute(query).fetchall())