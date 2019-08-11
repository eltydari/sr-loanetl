# -- FILE: loan_etl/db/schema/table_status.py
'''
Defines the schema for the status table
'''
from   .base import BaseTable, MODE_INSERT, PAT_NAME
from   .table_loans import Loans
from   sqlalchemy import (Column, BigInteger, String, 
                            Date, Numeric)
from   sqlalchemy.orm import relationship
from   sqlalchemy.schema import ForeignKeyConstraint
                            
class Status(BaseTable):
    __tablename__   = PAT_NAME.match(__name__).groups()[0]

    LoanId        = Column("loan_id", BigInteger(), primary_key=True)
    PlatformName  = Column("platform_name", String(255), primary_key=True)
    RecordDate    = Column("record_date", Date(), primary_key=True)
    PrincipalPaid = Column("principal_paid", Numeric(precision=15, scale=2), nullable=False)
    InterestPaid  = Column("interest_paid", Numeric(precision=15, scale=2), nullable=False)
    LoanStatus    = Column("loan_status", String(255), nullable=False)
    Loan          = relationship("Loans", backref="status")

    __table_args__ = (ForeignKeyConstraint([LoanId, PlatformName],
                                           [Loans.LoanId, Loans.PlatformName]), {})

    def __init__(self, loan_id, platform_name, record_date, 
                       principal_paid,
                       interest_paid,
                       loan_status):
        self.LoanId        = loan_id
        self.PlatformName  = platform_name
        self.RecordDate    = record_date
        self.PrincipalPaid = principal_paid
        self.InterestPaid  = interest_paid
        self.LoanStatus    = loan_status
                                           
    @property
    def mode(self):
        # Insert mode
        return MODE_INSERT

    def __repr__(self):
        return "<{0} | Id: {1} | Platform: {2} | Date: {3}>".format(
            self.__class__.__name__,
            self.LoanId,
            self.PlatformName,
            self.RecordDate)