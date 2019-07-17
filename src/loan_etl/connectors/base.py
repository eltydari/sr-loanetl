# -- FILE: src/loan_etl/connectors/base.py
from abc import ABC, abstractmethod

class ConnectorBase(ABC):
 
    def __init__(self, configuration):
        self.config = configuration
        super().__init__()
    
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass