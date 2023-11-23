# README
# Demo Video: https://youtu.be/sXausJVcNJM

## Setup Instructions for the Database

Before you can run the application, you need to set up the PostgreSQL database. Follow these steps:

### 1. Install PostgreSQL

If you haven't already installed PostgreSQL, please download and install it from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/)

### 2. Create the Database and User
The `create_db.sh` script will create a database named `mydatabase`, a user named `lucaswhitaker` (change this to your user) with the password `mypassword`, and grant the necessary privileges to the user. It will also create the `students` table and insert some initial data.

#### Configuration variables
```bash
DB_NAME="mydatabase"
DB_USER="insert_your_username"
DB_PASSWORD="mypassword"
```
In your terminal or command prompt, navigate to the directory containing the `create_db.sh` file. Then, run the following command to create the database and user:

```bash
./create_db.sh
```

## Steps to Compile and Run Your Application

To compile and run the application, follow these steps:

### 1. Install Required Python Libraries

Make sure you have Python installed on your system. Additionally, install the `psycopg2` library, which is used for connecting to the PostgreSQL database. You can install it using pip:

```bash
pip install psycopg2
```

### 2. Run the Python Application

In your terminal or command prompt, navigate to the directory containing the `main.py` file. Then, run the following command to start the application:

```bash
python main.py
```

The application will display a menu with options to interact with the database.

## Explanation of Each Function in the Application

Here's a brief explanation of each function in the application:

### 1. `connect_to_database()`

This function establishes a connection to the PostgreSQL database using the configuration provided in the `db_config` dictionary. It returns a database connection object or `None` if there's an error.

### 2. `getAllStudents()`

This function retrieves and displays all students from the `students` table in the database. It connects to the database, executes a SQL query, fetches the results, and prints them to the console.

### 3. `addStudent(first_name, last_name, email, enrollment_date)`

This function allows you to add a new student to the `students` table. It takes the student's information as input parameters, connects to the database, executes an SQL `INSERT` query, and commits the transaction.

### 4. `updateStudentEmail(student_id, new_email)`

This function updates a student's email address in the `students` table. It takes the student's ID and the new email as input parameters, connects to the database, executes an SQL `UPDATE` query, and commits the transaction. It checks if the update was successful and provides appropriate feedback.

### 5. `deleteStudent(student_id)`

This function deletes a student from the `students` table based on their ID. It takes the student's ID as an input parameter, connects to the database, executes an SQL `DELETE` query, and commits the transaction. It checks if the deletion was successful and provides appropriate feedback.
