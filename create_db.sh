#!/bin/bash

# Configuration variables
DB_NAME="mydatabase"
DB_USER="lucaswhitaker"
DB_PASSWORD="mypassword"

# Check if the database exists
if psql -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME"; then
  echo "Database '$DB_NAME' already exists. Deleting it..."
  dropdb "$DB_NAME"
fi

# Create the database
echo "Creating database '$DB_NAME'..."
createdb "$DB_NAME"

# Create a user and grant privileges
echo "Creating user '$DB_USER'..."
psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"

echo "Granting privileges to user '$DB_USER'..."
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

# Create tables
echo "Creating tables in '$DB_NAME'..."
psql -d "$DB_NAME" -f create_tables.sql

# Insert initial data
echo "Inserting initial data into 'students' table..."
psql -d "$DB_NAME" -c "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"

echo "Database setup complete."
