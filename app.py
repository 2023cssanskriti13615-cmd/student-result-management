import pandas as pd

students = pd.read_csv("students.csv")

while True:

    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Display all students")
    print("2. Search student by ID")
    print("3. Filter students by department")
    print("4. Add new student")
    print("5. Find student with highest marks")
    print("6. Calculate average marks")
    print("7. Display passed students")
    print("8. Display scholarship eligible students")
    print("9. Department-wise average marks")
    print("10. Display Pass/Fail status")
    print("11. Exit")

    choice = input("Enter your choice: ")

    # 1. Display all students
    if choice == "1":
        print("\nAll Students:")
        print(students)

    # 2. Search student by ID
    elif choice == "2":
        try:
            student_id = int(input("Enter student ID: "))

            result = students[students["id"] == student_id]

            if result.empty:
                print("Student not found.")
            else:
                print("\nStudent Found:")
                print(result)

        except ValueError:
            print("Invalid ID! Please enter a number.")

    # 3. Filter by department
    elif choice == "3":
        department = input("Enter department: ")

        result = students[
            students["department"].str.lower() == department.lower()
        ]

        if result.empty:
            print("No students found in this department.")
        else:
            print("\nStudents in", department)
            print(result)

    # 4. Add new student
    elif choice == "4":
        print("\nAdd New Student")

        name = input("Enter student name: ")
        department = input("Enter department: ")

        try:
            marks = float(input("Enter marks: "))
            attendance = float(input("Enter attendance: "))

            new_id = students["id"].max() + 1

            new_student = {
                "id": new_id,
                "name": name,
                "department": department,
                "marks": marks,
                "attendance": attendance
            }

            students.loc[len(students)] = new_student

            students.to_csv("students.csv", index=False)

            print("Student added successfully!")
            print("New Student ID:", new_id)

        except ValueError:
            print("Invalid input! Marks and attendance must be numbers.")

    # 5. Highest marks
    elif choice == "5":
        highest = students.loc[students["marks"].idxmax()]

        print("\nStudent with Highest Marks:")
        print(highest)

    # 6. Average marks
    elif choice == "6":
        average = students["marks"].mean()

        print("\nAverage Marks:", average)

    # 7. Passed students
    elif choice == "7":
        passed = students[students["marks"] >= 40]

        if passed.empty:
            print("No student has passed.")
        else:
            print("\nPassed Students:")
            print(passed)

    # 8. Scholarship eligible students
    elif choice == "8":
        scholarship = students[
            (students["marks"] >= 85) &
            (students["attendance"] >= 85)
        ]

        if scholarship.empty:
            print("No scholarship eligible students.")
        else:
            print("\nScholarship Eligible Students:")
            print(scholarship)

    # 9. Department-wise average
    elif choice == "9":
        department_average = students.groupby("department")["marks"].mean()

        print("\nDepartment-wise Average Marks:")
        print(department_average)

    # 10. Pass/Fail status
    elif choice == "10":
        result = students.copy()

        result["status"] = result["marks"].apply(
            lambda x: "Pass" if x >= 40 else "Fail"
        )

        print("\nStudent Pass/Fail Status:")
        print(result)

    # 11. Exit
    elif choice == "11":
        print("Thank you for using Student Result Management System!")
        break

    # Invalid menu choice
    else:
        print("Invalid choice! Please select 1-11.")