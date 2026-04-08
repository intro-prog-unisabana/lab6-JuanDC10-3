def student_averages(students):
    result = {}
    for student, grades in students.items():
        total = 0
        count = 0 
        for score in grades.values():
            total += score
            count += 1
        avg = round(total / count)
        result[student] = avg
    return result
def assignment_averages(students):
    result = {}
    for assignment in list(students.values())[0].keys():
        total = 0
        count = 0
        for grades in students.values():
            total += grades[assignment]
            count += 1
        avg = round(total / count)
        result[assignment] = avg
    return result