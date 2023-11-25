DEMO:
https://youtu.be/69k_CcG-MSE

Dependencies:
- Python 3.9.6
- psycopg2 

Setup:
- Initialize the database on PostgreSQL with the following parameters:
    dbname="student_records_updated",
    user="postgres",
    password="database", 
    host="localhost", 
    port="5432" 
Note: This can be change to any value when creating the database, however they should also be change on the python file

Instructions:
- The query tool should be compile and run with (ctrl + f5) or with the integrated run button on the text editor
- Functions are commented out to avoid erors while using the query tool
- Uncomment the function you would like to test to see output and functionality (*BE MINDFUL THAT THE ORDER ON WHICH YOU RUN THE FUNCTIONS IS IMPORTANT*)

Summary of functions: 
-getAllStudents(): 
Retrieves and prints all student records from the database

-addStudent(first_name, last_name, email, enrollment_date): 
Adds a new student to the database based on 4 parameters

- updateStudentEmail(student_id, new_email):
Updates the email address for a specific student based on their unique ID

- deleteStudent(student_id): 
Removes a student's record from the database based on a students unique ID