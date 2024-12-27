-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- First, remove any existing privileges for the user
-- This ensures we start with a clean state
REVOKE ALL PRIVILEGES, GRANT OPTION
FROM 'hbnb_test'@'localhost';

-- Grant all privileges on hbnb_test_db to the user
GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
