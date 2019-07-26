# -- FILE: src/loan_etl/connectors/csv_connector.py
'''
Defines the CSV data connector.
'''
from   .base import ConnectorBase
import csv
import os.path
import pandas as pd

class CsvConnector(ConnectorBase):
    
    def __init__(self, filePath, delimiter = ','):
        super().__init__()
        self.filePath = filePath
        self.delimiter = delimiter
        self._headers = []
        self._file = None
        self._csvreader = None
        self._processed = None

    @property
    def contents(self):
        df = pd.DataFrame(columns = self._headers)
        if self._processed:
            pass
        if self._csvreader:
            self._file.seek(0)
            next(self._csvreader, None)
            for row in self._csvreader:
                df = df.append(row, ignore_index=True)
        return df

    def load(self):
        self._file = open(self.filePath, newline='')
        self._csvreader = csv.DictReader(self._file, delimiter = self.delimiter)
        self._headers = self._csvreader.fieldnames
        return self

    def transform(self, mapinfo=None):
        return self