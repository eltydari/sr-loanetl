# -- FILE: features/orchestration.feature
Feature: Pipeline Configuration Files
  The ETL pipeline should consult a list of configuration 
  files which help orchestrate functionality in the ETL process
  for each data source.

  Background: We have an environment with a db and local machine
    Given we have a folder
      And a database

  Scenario: Basic end-to-end pipeline
    I should be able to run a command on the file and see the
    data populated in the database. This command should be
    runnable by an automated scheduler.

    Given a file named "test.csv" with:
      '''
      header1,header2,header3
      a1,b1,c1
      a2,b2,c2
      '''
      And a table named "testtable" with the following headers:
      '''
      official_header1
      official_header2
      official_header3
      '''
      And a file named "config.json", with the "%s" placeholder representing my folder path:
      '''
      {
         "streaming_size": 1000,
         "db":{
            "dbtype": "sqlite",
            "url": "",
            "username": "",
            "password": ""
         },
         "data":{
            "dataType": "csv",
            "connectorArgs":{
               "path": "%s/test.csv",
               "delimiter": ","
            },
            "mapping":{
               "official_header1":{
                  "sourceColumn": "header1",
                  "transformation": null,
                  "destTables": ["testtable"]
               },
               "official_header2":{
                  "sourceColumn": "header2",
                  "transformation": null,
                  "destTables": ["testtable"]
               },
               "official_header3":{
                  "sourceColumn": "header3",
                  "transformation": null,
                  "destTables": ["testtable"]
               }
            }
         }
      }
      '''
     When I run the following command, with the placeholder representing my folder path:
      '''
      run.py {folder_path}
      '''
      And I query the database with "SELECT * FROM testtable"
     Then I will see the following table:
      | 0  | 1  | 2  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |
