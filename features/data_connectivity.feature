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

    Given a file named "test.csv" with:
      '''
      header1,header2,header3
      a1,b1,c1
      a2,b2,c2
      '''
     When I use the csv connector to load data from "test.csv"
     Then I will see the following table:
      | header1  | header2  | header3  |
      | a1       | b1       | c1       |
      | a2       | b2       | c2       |
    
  Scenario: Streaming a CSV file
    I should be able to stream a set number of data records from
    my csv file.

    Given a file named "test.csv" with:
      '''
      header1,header2,header3
      a1,b1,c1
      a2,b2,c2
      a3,b3,c3
      a4,b4,c4
      a5,b5,c5
      '''
     When I use the csv connector to stream 2 rows from "test.csv"
     Then I will see the following table:
      | header1  | header2  | header3  |
      | a1       | b1       | c1       |
      | a2       | b2       | c2       |
     When I use the csv connector to stream 3 rows from "test.csv"
     Then I will see the following table:
      | header1  | header2  | header3  |
      | a3       | b3       | c3       |
      | a4       | b4       | c4       |
      | a5       | b5       | c5       |
  
  Scenario: Streaming Multiple CSV files
    I should be able to stream a data records from multiple csv files
    that share a folder designated by the configuration file.
    
    Given a file named "test1.csv" with:
      '''
      header1,header2,header3
      a1,b1,c1
      a2,b2,c2
      a3,b3,c3
      '''
      And a file named "test2.csv" with:
      '''
      header1,header2,header3
      a4,b4,c4
      a5,b5,c5
      '''
     When I use the csv connector to stream 2 rows from the folder
     Then I will see the following table:
      | header1  | header2  | header3  |
      | a1       | b1       | c1       |
      | a2       | b2       | c2       |
     When I use the csv connector to stream 3 rows from the folder
     Then I will see the following table:
      | header1  | header2  | header3  |
      | a3       | b3       | c3       |
      | a4       | b4       | c4       |
      | a5       | b5       | c5       |

  Scenario: Advanced CSV files (with configurations)
    If I supply a custom transformation configuration (map) while loading
    in a csv file, I should receive a transformed table in Python format.

    Given a file named "test.csv" with:
      '''
      header1,header2,header3
      yes,1,sally
      no,8.0,charlie
      no,.8,bee
      '''
    And a configuration map with the following representation:
      '''
      {
        "official_header1":{
          "sourceColumn": "header1",
          "transformation": "lambda x: True if x==\"yes\" else False"
        },
        "official_header2":{
          "sourceColumn": "header2",
          "transformation": "lambda x: float(x) + 1"
        },
        "official_header3":{
          "sourceColumn": "header3",
          "transformation": null
        }
      }
      '''
    When I use the csv connector with the map to load data from "test.csv"
    Then I will see the following table:
      | official_header1 | official_header2 | official_header3 |
      | True             | 2.0              | sally            |
      | False            | 9.0              | charlie          |
      | False            | 1.8              | bee              |

  Scenario: Advanced CSV files part 2 (with custom extra fields)
    If I supply a custom transformation configuration containing an 
    extra field, I should see the field as an additional in my 
    column in my resulting table.

    Given a file named "test.csv" with:
      '''
      header1
      yes
      no
      no
      '''
    And a configuration map with the following representation:
      '''
      {
        "official_header1":{
          "sourceColumn": "header1",
          "transformation": "lambda x: True if x==\"yes\" else False"
        },
        "official_header2":{
          "sourceColumn": null,
          "transformation": "lambda x: \"hello world!\""
        }
      }
      '''
    When I use the csv connector with the map to load data from "test.csv"
    Then I will see the following table:
      | official_header1 | official_header2 |
      | True             | hello world!     |
      | False            | hello world!     |
      | False            | hello world!     |