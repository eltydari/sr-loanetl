Implementation Plan
===================

This plan will consist of two parts: (1) the database schema, and (2) the architecture for the ETL application.


## Schema

The following represents the basic schema as an ER diagram which includes the essential datapoints. This schema may be updated after the MVP. Note that "Principal remaining" has been omitted as it is a computed value of "orginal balance" and "principal paid". Also note that "Loan Status" is a repeated attribute among both tables: this is intentional to provide insight on overall loan status vs specific time at which loan status changed.

![Schema](images/schema.png)

The data will be an aggregate of data across all platforms. The schema will consist of 2 tables which establish a relationship between a loan and its periodic status updates.  New attributes have been created as follows:

* Platform name (loan table) - the unique identifier for the platform.
* Record date (status table) - date at which record was generated, this can either be
