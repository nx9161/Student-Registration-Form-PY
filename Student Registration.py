import csv
import os


class Student:
    def __init__(self, studentId, name, age, grade):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.grade = grade


class CSVHandler:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['studentId', 'name', 'age', 'grade']
        if not os.path.isfile(csv_file):
            self.write_header()

    def write_header(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def addStudent(self, student):
        file_empty = os.stat(self.csv_file).st_size == 0
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            if file_empty:
                writer.writeheader()
            writer.writerow(vars(student))
        print("Student created successfully!")

    def getStudent(self, studentId):
        with open(self.csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['studentId'] == studentId:
                    return Student(**row)
        return None

    def updateStudent(self, student):
        updated = False
        rows = []
        with open(self.csv_file, 'r', newline='') as readFile:
            reader = csv.DictReader(readFile)
            rows = list(reader)

        for i, row in enumerate(rows):
            if row['studentId'] == student.studentId:
                rows[i].update({'name': student.name, 'age': student.age, 'grade': student.grade})
                updated = True
                break

        if updated:
            with open(self.csv_file, 'w', newline='') as writeFile:
                writer = csv.DictWriter(writeFile, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print("Student updated successfully!")
        else:
            print("Student not found!")

    def deleteStudent(self, studentId):
        deleted = False
        rows = []

        with open(self.csv_file, 'r', newline='') as readFile:
            reader = csv.DictReader(readFile)
            rows = list(reader)

        for i, row in enumerate(rows):
            if row['studentId'] == studentId:
                del rows[i]
                deleted = True
                break

        if deleted:
            with open(self.csv_file, 'w', newline='') as writeFile:
                writer = csv.DictWriter(writeFile, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print("Student information deleted successfully!")
        else:
            print("Student not found!")

    def print(self, student):
        print(f"Student Id: {student.studentId}")
        print(f"Student Name: {student.name}")
        print(f"Student Age: {student.age}")
        print(f"Student Grade: {student.grade}")


if __name__ == "__main__":
    csv_file = "Student Record.csv"
    fileHandler = CSVHandler(csv_file)
    while True:
        print("\nStudent Registration System")
        print("1. Create Student")
        print("2. Update Student Info")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            studentId = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade (A, B, C, F): ").upper()
            fileHandler.addStudent(Student(studentId, name, age, grade))
        elif choice == "2":
            studentId = input("Enter student ID: ")
            name = input("Enter new student name: ")
            age = input("Enter new student age: ")
            grade = input("Enter new student grade (A, B, C, F): ").upper()
            student = Student(studentId, name, age, grade)
            fileHandler.updateStudent(student)
        elif choice == "3":
            studentId = input("Enter student ID: ")
            fileHandler.deleteStudent(studentId)
        elif choice == "4":
            studentId = input("Enter student ID: ")
            student = fileHandler.getStudent(studentId)
            if student:
                fileHandler.print(student)
            else:
                print("Student not found!")
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
