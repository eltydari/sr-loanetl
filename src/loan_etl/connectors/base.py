# -- FILE: src/loan_etl/connectors/base.py
'''
Defines the data connector prototype class.
'''
from abc import ABC, abstractmethod

class ConnectorBase(ABC):
 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass