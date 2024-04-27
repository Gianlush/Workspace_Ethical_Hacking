CREATE DATABASE IF NOT EXISTS vulnapp;
USE vulnapp;

CREATE TABLE IF NOT EXISTS users (
  username VARCHAR(50) PRIMARY KEY NOT NULL,
  password VARCHAR(100) NOT NULL,
  info	   VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password, info) VALUES ('administrator', 'ethical-test-2022', '3cr9Ae');

