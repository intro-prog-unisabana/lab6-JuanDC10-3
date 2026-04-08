def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}
def add_student(student_grades={}):
    name = input("Enter student name:\n").title()
    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n")  
        if entry.lower() == "exit":
            break 
        subject, grade = entry.split(",")
        subjects[subject.title()] = float(grade)  
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades
def get_students(student_grades, keys):
    result = {} 
    for key in keys:
        found = False 
        for student in student_grades:
            if student.lower() == key.lower():
                result[student] = student_grades[student]
                found = True
                break  
        if not found:
            print(key.title(), "not found!") 
    return result
def calculate_averages(student_grades):
    result = {}
    for student, grades in student_grades.items():
        total = 0
        count = 0
        for score in grades.values():
            total += score
            count += 1
        if count == 0:
            result[student] = 0
        else:
            result[student] = round(total / count)
    return result
def print_students(student_grades):
    for student, grades in student_grades.items():
        print(student + ":")
        
        if len(grades) == 0:
            print("  No subjects")
        else:
            for subject, score in grades.items():
                print(" ", subject + ":", score)