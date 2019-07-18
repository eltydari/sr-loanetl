# -- FILE: features/data_connectivity.feature
Feature: Data Connectivity

    The ETL pipeline should define connectors to data source types. 
    These connectors should transform source data format into a 
    common intermediate format for loading into the database.

    Scenario: CSV files
        Given a file named "example.csv" with:
            '''
            "a","b","c"
            "a1","b1","c1"
            "a2","b2","c2"
            '''
         When I run the csv connector on "example.csv"
         Then I will see the following table:
            | a  | b  | c  |
            | a1 | b1 | c1 |
            | a2 | b2 | c2 |