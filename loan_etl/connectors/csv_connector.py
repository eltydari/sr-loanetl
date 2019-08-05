# -- FILE: loan_etl/connectors/csv_connector.py
'''
Defines the CSV data connector.
'''
from   .base import ConnectorBase
import csv
import os
import os.path
import pandas as pd

class CSVConnector(ConnectorBase):
    
    def __init__(self, path, delimiter = ','):
        super().__init__()
        self._delimiter = delimiter
        self._headers   = []
        self._rawData = None
        self._processedData = None
        self._streamer  = None

        self._path = path
        self._files = []
        if os.path.isdir(self._path):
            fileNames = next(os.walk(self._path))[2]
            for fileName in fileNames:
                f = open(os.path.join(path, fileName), newline='')
                self._files.append(f)
        else:
            self._files.append(open(path, newline=''))

    @property
    def path(self):
        # Returns the path to the csv files
        return self._path

    def stream(self, chunksize=1000):
        # Returns the data in chunks
        if not self._streamer:
            self._streamer = self._sourceData()
        df = pd.DataFrame(columns = self._headers)
        for _ in range(chunksize):
            row = next(self._streamer, None)
            if not row:
                return df
            df = df.append(row, ignore_index=True)
        return df

    def load(self):
        # Loads the data as raw data
        def generate():
            for f in self._files:
                csvreader = csv.DictReader(f, delimiter = self._delimiter)
                self._headers = csvreader.fieldnames
                for row in csvreader:
                    yield row

        self._rawData = generate()
        self._processedData = None
        return self

    def transform(self, mapping={}):
        # Transforms the data into processed data
        if mapping:
            self._headers = mapping.keys()

            def generate():
                for row in self._rawData:
                    new_row = {}
                    for k,v in mapping.items():
                        cell = row.get(v["sourceColumn"], None)
                        # Potential security vulnerability; alternatives out of scope
                        transform = v["transformation"]
                        if transform and transform[:6] != "lambda":
                            raise Exception("Transformation provided was not a lambda")
                        func = eval(transform) if transform else lambda x: x
                        new_row[k] = func(cell)
                    yield new_row
                    
            self._processedData = generate()
        return self

    def _sourceData(self):
        if self._processedData:
            return self._processedData
        elif self._rawData:
            return self._rawData
        return []