# -- FILE: loan_etl/connectors/csv_connector.py
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
        # Flattens and returns the data
        df = pd.DataFrame(columns = self._headers)
        source = []
        if self._processed:
            source = self._processed
        elif self._csvreader:
            self._file.seek(0)
            next(self._csvreader, None)
            source = self._csvreader
        for row in source:
            df = df.append(row, ignore_index=True)
        return df

    def load(self):
        self._file = open(self.filePath, newline='')
        self._csvreader = csv.DictReader(self._file, delimiter = self.delimiter)
        self._headers = self._csvreader.fieldnames
        return self

    def transform(self, mapinfo=None):
        if mapinfo:
            # Generator saves memory space for large datasets
            def data_gen(data):
                for row in data:
                    new_row = {}
                    for key, value in mapinfo.items():
                        cell = row[value["source"]]
                        # Potential security vulnerability; alternatives out of scope
                        func = eval(value["transformation"]) if value["transformation"] else lambda x: x
                        new_row[key] = func(cell)
                    yield new_row
            self._headers = mapinfo.keys()
            self._processed = data_gen(self._csvreader)
        return self