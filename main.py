import psycopg2
from psycopg2 import Error

# Database connection configuration
db_config = {
    "host": "localhost",
    "database": "mydatabase",
    "user": "lucaswhitaker",
    "password": "mypassword"
}

# Function to connect to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to retrieve and display all students
def getAllStudents():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students;")
            students = cursor.fetchall()
            for student in students:
                print(student)
        except Error as e:
            print(f"Error retrieving students: {e}")
        finally:
            cursor.close()
            conn.close()

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date)
            )
            conn.commit()
            print("Student added successfully.")
        except Error as e:
            print(f"Error adding student: {e}")
        finally:
            cursor.close()
            conn.close()

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id)
            )
            conn.commit()
            if cursor.rowcount == 1:
                print("Email updated successfully.")
            else:
                print("Student not found.")
        except Error as e:
            print(f"Error updating email: {e}")
        finally:
            cursor.close()
            conn.close()

# Function to delete a student
def deleteStudent(student_id):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM students WHERE id = %s;",
                (student_id,)
            )
            conn.commit()
            if cursor.rowcount == 1:
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        except Error as e:
            print(f"Error deleting student: {e}")
        finally:
            cursor.close()
            conn.close()

# Main program
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update student's email")
        print("4. Delete a student")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            deleteStudent(student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
