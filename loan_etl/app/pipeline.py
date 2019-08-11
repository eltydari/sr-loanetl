# -- FILE: loan_etl/app/pipeline.py
'''
Runs the ETL pipeline
'''
from   ..connectors import getConnector
from   ..db import DBLoader, getSchema
import json
import os

def runPipeline(config):
    streaming_size = config["streaming_size"]
    connectorType  = config["data"]["dataType"]
    connectorArgs  = config["data"]["connectorArgs"]
    dataMap        = config["data"]["mapping"]
    dbArgs         = config["db"]

    connector = getConnector(connectorType, **connectorArgs)
    db = DBLoader(**dbArgs)

    dataConnector = connector.load().transform(dataMap)
    dstream = None
    while True:
        dstream = dataConnector.stream(streaming_size)
        if dstream.empty:
            break
        retval = db.load(dstream, mapping=dataMap)

def run(configDir):
    files = next(os.walk(configDir))[2]
    filePaths = (os.path.join(configDir, f) for f in files)
    for filePath in filePaths:
        if os.path.splitext(filePath)[1] == ".json":
            with open(filePath) as f:
                cfg = json.load(f)
                runPipeline(cfg)