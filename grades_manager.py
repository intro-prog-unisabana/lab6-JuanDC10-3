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
