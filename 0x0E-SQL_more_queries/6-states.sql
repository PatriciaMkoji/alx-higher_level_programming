-- script that creates the database hbtn_0d_usa &
-- table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	       id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	       name VARCHAR(256) NOT NULL
);
