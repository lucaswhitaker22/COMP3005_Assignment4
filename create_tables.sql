-- create_tables.sql

CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    enrollment_date DATE
);