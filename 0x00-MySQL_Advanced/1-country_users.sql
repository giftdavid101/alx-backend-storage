-- Script creates table users with the attributes below
-- id, name, email and country

CREATE TABLE IF NOT EXITS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255) NOT NULL,
	country ENUM('US','CO','TN',) NOT NULL
);
