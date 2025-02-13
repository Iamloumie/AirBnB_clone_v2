-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- First, remove any existing privileges for the user
-- This ensures we start with a clean slate
REVOKE ALL PRIVILEGES, GRANT OPTION
FROM 'hbnb_dev'@'localhost';

-- Grant all privileges on hbnb_dev_db to the user
GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
