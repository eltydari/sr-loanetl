# -- FILE: loan_etl/db/schema/table_loans.py
'''
Defines the schema for the loan table
'''
from   .base import BaseTable, MODE_UPDATE, PAT_NAME
from   sqlalchemy import (Column, BigInteger, String, 
                            Date, Float, Numeric)

class Loans(BaseTable):
    __tablename__   = PAT_NAME.match(__name__).groups()[0]

    LoanId          = Column("loan_id", BigInteger(), primary_key=True)
    PlatformName    = Column("platform_name", String(255), primary_key=True)
    IssueDate       = Column("issue_date", Date(), nullable=False)
    OriginalBalance = Column("original_balance", Numeric(precision=15, scale=2), nullable=False)
    InterestRate    = Column("interest_rate", Float(), nullable=False)
    PlatformRating  = Column("platform_rating", String(255), nullable=False)
    LoanStatus      = Column("loan_status", String(255), nullable=False)

    def __init__(self, loan_id, platform_name, 
                       issue_date, 
                       original_balance, 
                       interest_rate, 
                       platform_rating,
                       loan_status):
        self.LoanId          = loan_id
        self.PlatformName    = platform_name
        self.IssueDate       = issue_date
        self.OriginalBalance = original_balance
        self.InterestRate    = interest_rate
        self.PlatformRating  = platform_rating
        self.LoanStatus      = loan_status

    @property
    def mode(self):
        # Update mode
        return MODE_UPDATE

    def __repr__(self):
        return "<{0} | Id: {1} | Platform: {2}>".format(
            self.__class__.__name__,
            self.LoanId,
            self.PlatformName)