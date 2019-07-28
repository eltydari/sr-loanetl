# -- FILE: features/db_connectivity.feature
@skip
Feature: Database Connectivity
  The ETL pipeline should be able to be configured
  to load data to multiple destinations

  Background: We have a database
    Given a database

  Scenario: Basic database loading
     When I load the following table:
      | a  | b  | c  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |
      And I query the database with ""
     Then I will see the following table:
      | a  | b  | c  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |


  '''Scenario: Postgres database
    Given a new Postgres database
     When I load the following table:
      | a  | b  | c  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |
      And I call ""
     Then I will see the following table:
      | a  | b  | c  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |'''