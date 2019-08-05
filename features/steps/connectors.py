# -- FILE: features/steps/connectors.py
import csv
import os.path
from   loan_etl.connectors import getConnector

def getContextConnector(context, connectorType, fileName):
    if not hasattr(context, "connectors"):
        context.connectors = {}
    return context.connectors.setdefault((connectorType, fileName),\
                                          getConnector(connectorType, fileName))

@when(u"I use the {connectorType} connector to load data from \"{fileName}\"")
def when_load_data_from_csv(context, connectorType, fileName):
    connector = getContextConnector(context, connectorType, 
                                    os.path.join(context.dir.name, fileName))
    context.result = connector.load().stream()

@when(u"I use the {connectorType} connector to stream {stream_size} rows from \"{fileName}\"")
def when_stream_data_from_csv(context, connectorType, stream_size, fileName):
    stream_size = int(stream_size)
    connector = getContextConnector(context, connectorType, 
                                    os.path.join(context.dir.name, fileName))
    context.result = connector.load().transform().stream(stream_size)

@when(u"I use the {connectorType} connector to stream {stream_size} rows from the folder")
def when_stream_multi_data_from_csv(context, connectorType, stream_size):
    stream_size = int(stream_size)
    connector = getContextConnector(context, connectorType,
                                    context.dir.name)
    context.result = connector.load().transform().stream(stream_size)

@when(u"I use the {connectorType} connector with the map to load data from \"{fileName}\"")
def when_load_data_from_csv(context, connectorType, fileName):
    connector = getContextConnector(context, connectorType, 
                                    os.path.join(context.dir.name, fileName))
    context.result = connector.load().transform(context.cfg).stream()