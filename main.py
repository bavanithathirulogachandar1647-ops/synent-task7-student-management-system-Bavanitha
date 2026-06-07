import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "age": input("Enter Student Age: "),
        "course": input("Enter Student Course: ")
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")


def view_students():
    students = load_students()

    if len(students) == 0:
        print("No Student Records Found!")
        return

    print("\nStudent Records:")
    print("-" * 40)

    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print("-" * 40)


def update_student():
    students = load_students()

    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            save_students(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to Delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")