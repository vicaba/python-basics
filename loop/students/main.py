def main():
    # Create a dictionary with students and their grades
    students = {'Peter': 85, 'Anna': 92, 'Luis': 78, 'Maria': 95}

    # Print the entire dictionary
    print("Full dictionary:")
    print(students)

    # Use a loop to print each student's name and their corresponding grade
    for student, grade in students.items():
        print(f"{student} has a grade of {grade}.")

    # Add a new student and their grade to the dictionary
    students['Carlos'] = 89
    print("Dictionary after adding Carlos:")
    print(students)

    # Use a loop to calculate the average of the grades
    sum_grades = sum(students.values())
    average_grades = sum_grades / len(students)
    print(f"The average of the grades is {average_grades}.")

    # Find the student with the highest grade
    best_student = max(students, key=students.get)
    print(f"The student with the highest grade is {best_student} with {students[best_student]}.")

    # Remove a student from the dictionary
    del students['Luis']
    print("Dictionary after removing Luis:")
    print(students)

    # Check if a student is in your dictionary
    if 'Peter' in students:
        print("Peter is in the dictionary.")
    else:
        print("Peter is not in the dictionary.")

    # Print the number of students in the dictionary
    print("The number of students in the dictionary is:")
    print(len(students))

if __name__ == "__main__":
    main()