from grades_manager import *

print("Welcome to the Student Grades Manager!\n")

my_grades = {}

while True:
    print("Select an option:")
    print("1. Add a student")
    print("2. Print student grade averages")
    print("3. Exit")
    
    option = input()
    
    if option == "1":
        my_grades = add_student(my_grades)
    
    elif option == "2":
        print("Select an option:")
        print("a. Display all students")
        print("b. Display selected students")
        
        sub_option = input()
        
        if sub_option == "a":
            avg = calculate_averages(my_grades)
            for student, value in avg.items():
                print(student + ":", value)
        
        elif sub_option == "b":
            names = input("Enter student names (comma-separated):\n")
            names_list = names.split(",")
            
            selected = get_students(my_grades, names_list)
            avg = calculate_averages(selected)
            
            for student, value in avg.items():
                print(student + ":", value)
        
        else:
            print("Invalid option selected!")
    
    elif option == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option selected!")