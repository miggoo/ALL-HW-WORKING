DROP DATABASE IF EXISTS favorite_book;
-- Creates the "favorite_db" database --
CREATE DATABASE favorite_book;
USE favorite_book;

CREATE TABLE favorite_book (
  -- Make a string column called "song" which cannot contain null --
  title VARCHAR(50) NOT NULL,
  -- Make a string column called "artist" --
  id int AUTO_INCREMENT NOT NULL,
  -- Make an integer column called "score" --
  PRIMARY KEY(id)
);
select * FROM favorite_book;

CREATE TABLE authors (
  -- Make a string column called "song" which cannot contain null --
  firstname VARCHAR(50),
  -- Make a string column called "artist" --
  
  secondname VARCHAR(50),
  id int AUTO_INCREMENT NOT NULL,
  -- Make an integer column called "score" --
  PRIMARY KEY(id)
);

select * from authors