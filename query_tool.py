import psycopg2
from psycopg2 import sql

# Connecting to the database
connection = psycopg2.connect(
    dbname="student_records_updated",
    user="postgres",
    password="database", 
    host="localhost", 
    port="5432" 
)

# Creating selector to be able to perform tasks on the db
selector = connection.cursor()

# This function is able to retrieve all student in our db
def getAllStudents():
    selector.execute("SELECT * FROM students")
    students = selector.fetchall()
    for student in students:
        print(student)

# This function is able to add a new student to our db
def addStudent(first_name, last_name, email, enrollment_date):
    
    # SQL command to insert into table
    try:
        selector.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date)
        )
        connection.commit()
        print(f"Student {first_name} {last_name} added successfully.")

    # Error handling    
    except psycopg2.Error as error:
        print("Error while trying to add student to database: ", error)
        connection.rollback()

# This function is able to update a student's email
def updateStudentEmail(student_id, new_email):

    # SQL command to update value on table 
    try:
        selector.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )
        connection.commit()
        print(f"Email updated successfully.")

    # Error handling
    except psycopg2.Error as error:
        print("Error updating email: ", error)
        connection.rollback()

# This function is able to delete a student based on id parameter
def deleteStudent(student_id):
    
    # SQL command to delete row from table
    try:
        selector.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )
        connection.commit()
        print(f"Student deleted successfully.")

    # Error handling
    except psycopg2.Error as error:
        print("Error while trying to delete student: ", error)
        connection.rollback()

'''
Test Cases:
'''
#getAllStudents()
#addStudent('Tommy', 'Lee', 'mr_lee@cmail.ca', '2023-01-07')
#updateStudentEmail(1,'john_secret_email@cmail.com')
#deleteStudent(1)

# Good practice to finalize selector and connection to database
selector.close()
connection.close()