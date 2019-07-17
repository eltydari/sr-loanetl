# -- FILE: src/loan_etl/connectors/csv_connector.py
from .base import ConnectorBase

class CsvConnector(ConnectorBase):
    
    def __init__(self, configuration):
        super().__init__(configuration)

    def load(self):
        raise NotImplementedError

    def transform(self, data):
        raise NotImplementedError