# Student Registration System

This Python script provides a simple command-line interface for managing student records stored in a CSV file. It allows users to create, update, delete, and search for student information.

## Features

- **Create Student**: Add a new student to the records with a unique student ID, name, age, and grade.
- **Update Student Info**: Modify the details of an existing student by providing their ID and new information.
- **Delete Student**: Remove a student's record from the system by specifying their ID.
- **Search Student**: Retrieve and display information about a student based on their ID.
- **CSV Persistence**: Student records are stored in a CSV file, ensuring data persistence between sessions.

## Prerequisites

- Python 3.x
- CSV module (part of Python standard library)

## Usage

1. Clone the repository to your local machine:

git clone https://github.com/your_username/student-registration-system.git

2. Navigate to the project directory:

cd student-registration-system

3. Run the script:

python student_registration_system.py

4. Follow the on-screen prompts to interact with the student registration system.

## Usage Example

$ python student_registration_system.py

Student Registration System

Create Student

Update Student Info

Delete Student

Search Student

Exit

Enter your choice (1-5): 1

Enter student ID: 001

Enter student name: John Doe

Enter student age: 20

Enter student grade (A, B, C, F): A

Student created successfully!...

Exiting program. Goodbye!

## Note

- The CSV file storing student records is named "Student Record.csv". You can modify this filename in the script if needed.
- Ensure that you have appropriate permissions to read and write to the CSV file in the specified location.


