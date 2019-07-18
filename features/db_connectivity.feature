# -- FILE: features/db_connectivity.feature
Feature: Database Connectivity
  The ETL pipeline should define modular database connectors
  which will allow loading to multiple destinations and 
  database types.

  Scenario: Postgres database
    Given a new Postgres database
     When I load the following table:
      | a  | b  | c  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |
      And I call ""
     Then I will see the following table:
      | a  | b  | c  |
      | a1 | b1 | c1 |
      | a2 | b2 | c2 |