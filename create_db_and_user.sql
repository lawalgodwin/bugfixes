-- create the database to be used
DROP DATABASE IF EXISTS flask;
CREATE DATABASE flask;

-- create the user that will connect to our DB
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'nedutechboy';

-- let's grant our user root privilege to our DB

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';

-- let's switch to out DATABASE
USE flask;

-- create our table
CREATE TABLE IF NOT EXISTS info_table(
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256),
    age INT,
    PRIMARY KEY(id)
);

-- let's commit changes
FLUSH PRIVILEGES;
