# -- FILE: features/data_connectivity.feature
Feature: Data Connectivity
  The ETL pipeline should define connectors to data source types. 
  These connectors should transform source data format into a 
  common intermediate format for loading into the database.

  Background: We have a folder for storing files
    Given we have a folder

  Scenario: Basic CSV files
    I should be able to load in a basic csv file without any custom
    transformations and get the same table in Python format.

    Given a file named "example.csv" with:
      '''
      header1,header2,header3
      a1,b1,c1
      a2,b2,c2
      '''
     When I use the csv connector to load data from "example.csv"
     Then I will see the following table:
      | header1  | header2  | header3  |
      | a1       | b1       | c1       |
      | a2       | b2       | c2       |

  Scenario: CSV files with Configurations
    If I supply a custom transformation configuration (map) while loading
    in a csv file, I should receive a transformed table in Python format.

    Given a file named "custom.csv" with:
    '''
    header1,header2,header3
    yes,1,sally
    no,8.0,charlie
    no,.8,bee
    '''
    And a map with the following representation:
    '''
    {
      "official_header1":{
        "source": "header1",
        "transformation": "lambda x: True if x==\"yes\" else False"
      },
      "official_header2":{
        "source": "header2",
        "transformation": "lambda x: float(x)"
      },
      "official_header3":{
        "source": "header3",
        "transformation": null
      }
    }
    '''
    When I use the csv connector with the map to load data from "custom.csv"
    Then I will see the following table:
      | official_header1 | official_header2 | official_header3 |
      | True             | 1.0              | sally            |
      | False            | 8.0              | charlie          |
      | False            | 0.8              | bee              |