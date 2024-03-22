-- prepares a MySQL server for the project
-- create a database, a new user and grant privileges

CREATE DATABASE IF NOT EXISTS HBNB_DEV_DB;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON HBNB_DEV_DB.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON PERFORMANCE_SCHEMA.* TO 'hbnb_dev'@'localhost';