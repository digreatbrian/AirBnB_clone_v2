-- prepares a MySQL server for the project
-- create a database, a new user and grant privileges

CREATE DATABASE IF NOT EXISTS HBNB_TEST_DB;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON HBNB_TEST_DB.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON PERFORMANCE_SCHEMA.* TO 'hbnb_test'@'localhost';