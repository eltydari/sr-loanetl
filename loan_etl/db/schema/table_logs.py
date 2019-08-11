# -- FILE: loan_etl/db/schema/table_status.py
'''
Defines the schema for the logs table
'''
from   .base import BaseTable, MODE_INSERT, PAT_NAME
from   sqlalchemy import Column, BigInteger, String, Date

TABLENAME = "logs"

class Logs(BaseTable):
    __tablename__   = PAT_NAME.match(__name__).groups()[0]

    Id            = Column("id", BigInteger(), primary_key=True, unique=True)
    LoanId        = Column("loan_id", BigInteger())
    Message       = Column("message", String(255))
    Date          = Column("date", Date(), nullable=False)

    def __init__(self, id, loan_id, message, date):
        self.Id      = loan_id
        self.LoanId  = platform_name
        self.Message = issue_date
        self.Date    = original_balance

    @property
    def mode(self):
        # Insert mode
        return MODE_INSERT

    def __repr__(self):
        return "<{0} | Id: {1} | Date: {2}>".format(
            self.__class__.__name__,
            self.Id,
            self.Date)