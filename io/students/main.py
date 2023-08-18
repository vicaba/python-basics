def add_grade():
    name = input("Enter the student's name: ")
    grade = input("Enter the student's grade: ")
    f = open('student_grades.txt', 'a')
    f.write(f'{name}, {grade}\n')
    f.close()


def show_grades():
    f = open('student_grades.txt', 'r')
    print(f.read())
    f.close()


def calculate_average():
    with open('student_grades.txt', 'r') as f:
        lines = f.readlines()
        grades = [float(line.split(',')[1]) for line in lines]
        average = sum(grades) / len(grades)
        print(f'The average grade is: {average}')


def main():
    while True:
        print("\nStudent Grade Manager")
        print("1. Add grade for a student")
        print("2. Show all grades")
        print("3. Calculate average grade")
        print("4. Exit")
        option = input("Please enter your option: ")

        if option == '1':
            add_grade()
        elif option == '2':
            show_grades()
        elif option == '3':
            calculate_average()
        elif option == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == '__main__':
    main()
