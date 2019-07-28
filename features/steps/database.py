# -- FILE: features/steps/database.py
import loan_etl.db.loader as dbimpl

@given(u"a database")
def given_database(context):
    context.db = dbimpl.DbLoader()

