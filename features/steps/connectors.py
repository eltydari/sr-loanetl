# -- FILE: features/steps/connectors.py
import csv
import os.path
import loan_etl.connectors.csv_connector as csvc

def getConnector(context, fileName):
    if not hasattr(context, "connector"):
        filePath = os.path.join(context.dir.name, fileName)
        context.connector = csvc.CsvConnector(filePath)
    return context.connector

@when(u"I use the csv connector to load data from \"{fileName}\"")
def when_load_data_from_csv(context, fileName):
    connector = getConnector(context, fileName)
    context.result = connector.load().contents

@when(u"I use the csv connector to stream {stream_size} rows from \"{fileName}\"")
def when_stream_data_from_csv(context, stream_size, fileName):
    stream_size = int(stream_size)
    connector = getConnector(context, fileName)
    context.result = context.connector.load().transform().stream(stream_size)

@when(u"I use the csv connector with the map to load data from \"{fileName}\"")
def when_load_data_from_csv(context, fileName):
    connector = getConnector(context, fileName)
    context.result = connector.load().transform(context.cfg).contents