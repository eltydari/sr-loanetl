# -- FILE: src/loan_etl/connectors/csv_connector.py
'''
Defines the CSV data connector.
'''
from   .base import ConnectorBase
import csv
import os.path

class CsvConnector(ConnectorBase):
    
    def __init__(self, filePath, delimiter = ','):
        super().__init__()
        self.filePath = filePath
        self.delimiter = delimiter
        self.csvreader = None

    @property
    def contents(self):
        pass

    def load(self):
        with open(self.filePath, newline='') as csvfile:
            self.csvreader = csv.reader(csvfile, delimiter = self.delimiter)
        return self

    def transform(self, mapinfo):
        return self