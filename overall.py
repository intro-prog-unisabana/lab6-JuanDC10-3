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
        avg = round(total / count)
        result[assignment] = avg
    return result