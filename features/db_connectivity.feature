# -- FILE: features/db_connectivity.feature
@skip
Feature: Database Connectivity
  The ETL pipeline should be able to be configured
  to load data to multiple destinations

  Background: We have a database
    Given a database

  Scenario: Basic database loading
     When I load a table named "test" with the following:
      | header1  | header2  | header3  |
      | a1       | b1       | c1       |
      | a2       | b2       | c2       |
      And I query the database with "SELECT * FROM test"
     Then I will see the following table:
      | 0  | 1  | 2  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |