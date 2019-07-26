# -- FILE: src/loan_etl/connectors/csv_connector.py
'''
Defines the CSV data connector.
'''
from .base import ConnectorBase

class CsvConnector(ConnectorBase):
    
    def __init__(self, path=None, delimiter=','):
        super().__init__()

    @property
    def contents(self):
        pass

    def load(self, path=None):
        raise NotImplementedError

    def transform(self):
        raise NotImplementedError