# -- FILE: connectors/__init__.py
from .csv_connector import CSVConnector

connectors = {
    "csv": CSVConnector,
}

def getConnector(type, *args, **kwargs):
    connector = connectors.get(type)
    if not connector:
        raise KeyError(
            "Connector \"{}\" is not registered in the list of connectors"\
            .format(type))
    return connector(*args, **kwargs)