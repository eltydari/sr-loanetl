# -- FILE: src/loan_etl/connectors/csv_connector.py
'''
Defines the CSV data connector.
'''
from .base import ConnectorBase

class CsvConnector(ConnectorBase):
    
    def __init__(self, filePath, delimiter=','):
        super().__init__(configuration)

    def load(self):
        raise NotImplementedError

    def transform(self, data):
        raise NotImplementedError