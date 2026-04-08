def student_averages(students):
    result = {}
    for student, grades in students.items():
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
def assignment_averages(students):
    result = {}
    if len(students) == 0:
        return result
    for assignment in list(students.values())[0].keys():
        total = 0
        count = 0
        for grades in students.values():
            total += grades[assignment]
            count += 1
        result[assignment] = round(total / count)
    return result