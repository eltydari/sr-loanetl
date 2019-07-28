# -- FILE: loan_etl/connectors/base.py
'''
Defines the data connector prototype class.
'''
from abc import ABC, abstractmethod

class ConnectorBase(ABC):
 
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def contents(self):
        pass

    @abstractmethod
    def stream(self, chunksize):
        pass
    
    @abstractmethod
    def load(self):
        return self

    @abstractmethod
    def transform(self, mapinfo):
        return self
