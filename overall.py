def student_averages(students):
    result = {}
    for student, grades in students.items():
        total = 0
        for score in grades.values():
            total += score
        result[student] = total / len(grades)
    return result