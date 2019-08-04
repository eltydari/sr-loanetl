# -- FILE: features/db_connectivity.feature
Feature: Database Connectivity
  The ETL pipeline should be able to be configured
  to load data to multiple destinations

  Background: We have a database
    Given a database

  Scenario: Basic database loading
    I should be able to load a table into the database and 
    successfully query it with SQL.

    Given a table named "test" with the following headers:
      '''
      header1
      header2
      header3
      '''
     When I load the following into the database:
      | header1 | header2 | header3 |
      | a1      | b1      | c1      |
      | a2      | b2      | c2      |
      And I query the database with "SELECT * FROM test"
     Then I will see the following table:
      | 0  | 1  | 2  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |

  Scenario: Advanced database loading (with configuration)
    If I supply a custom configuration specifying the data
    be loaded into multiple tables, I should be able to query 
    table 1 and get my expected data.
    Note: Table names must be defined in schema.py beforehand

    Given a table named "test1" with the following headers:
      '''
      header1
      header2
      header3
      '''
      And a table named "test2" with the following headers:
      '''
      header1
      header4
      '''
      And a configuration map with the following representation:
      '''
      {
        "header1":{
          "destTables": ["test1", "test2"]
        },
        "header2":{
          "destTables": ["test1"]
        },
        "header3":{
          "destTables": ["test1"]
        },
        "header4":{
          "destTables": ["test2"]
        }
      }
      '''
      And I load, using the configuration, the following into the database:
      | header1 | header2 | header3 | header4 |
      | a1      | b1      | c1      | d1      |
      | a2      | b2      | c2      | d2      |
     When I query the database with "SELECT * FROM test1"
     Then I will see the following table:
      | 0  | 1  | 2  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |
     When I query the database with "SELECT * FROM test2"
     Then I will see the following table:
      | 0  | 1  |
      | a1 | d1 |
      | a2 | d2 |