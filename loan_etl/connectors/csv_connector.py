# -- FILE: loan_etl/connectors/csv_connector.py
'''
Defines the CSV data connector.
'''
from   .base import ConnectorBase
import csv
import os.path
import pandas as pd

class CSVConnector(ConnectorBase):
    
    def __init__(self, filePath, delimiter = ','):
        super().__init__()
        self.filePath = filePath
        self.delimiter = delimiter
        self._headers = []
        self._file = None
        self._csvreader = None
        self._processed = None
        self._transfMap = None
        self._streamer = None

    @property
    def contents(self):
        # Flattens and returns the data
        df = pd.DataFrame(columns = self._headers)
        dsource = self._sourceData()
        for row in dsource:
            df = df.append(row, ignore_index=True)
        return df

    def stream(self, chunksize=100, reset=False):
        # Returns the data in chunks
        df = pd.DataFrame(columns = self._headers)
        if not self._streamer or reset:
            self._streamer = self._sourceData()
        for _ in range(chunksize):
            row = next(self._streamer, None)
            if not row:
                return df
            df = df.append(row, ignore_index=True)
        return df

    def load(self):
        self._file = open(self.filePath, newline='')
        self._csvreader = csv.DictReader(self._file, delimiter = self.delimiter)
        self._headers = self._csvreader.fieldnames
        return self

    def transform(self, mapping=None):
        if mapping:
            self._transfMap = mapping
            self._headers = mapping.keys()
        return self

    def _transformImpl(self):
        # Generator saves memory space for large datasets
        def generate(data):
            for row in data:
                new_row = {}
                for key, value in self._transfMap.items():
                    cell = row.get(value["sourceColumn"], None)
                    # Potential security vulnerability; alternatives out of scope
                    func = eval(value["transformation"]) if value["transformation"] else lambda x: x
                    new_row[key] = func(cell)
                yield new_row
        return generate(self._csvreader)

    def _sourceData(self):
        self._file.seek(0)
        next(self._csvreader, None)

        if self._transfMap:
            return self._transformImpl()
        elif self._csvreader:
            return self._csvreader
        return []