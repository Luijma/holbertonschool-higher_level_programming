-- creates table hbtn_0d_usa with the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id));
