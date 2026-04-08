def student_averages(students):
    result = {}
    for student, grades in students:
        total = 0
        for score in grades:
            total += score
        result[student] = total / len(grades)
    return result