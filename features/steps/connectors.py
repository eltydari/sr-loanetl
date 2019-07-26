# -- FILE: features/steps/ops_file.feature
import csv
import os.path
import src.loan_etl.connectors.csv_connector as csvc

@when(u"I use the csv connector to load data from \"{fileName}\"")
def when_load_data_from_csv(context, fileName):
    dir = context.dir.name
    filePath = os.path.join(dir, fileName)
    connector = csvc.CsvConnector(filePath)
    context.result = connector.load().contents