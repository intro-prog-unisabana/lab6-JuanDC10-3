# Write your code here!
def employee_print(employee_info):
    name = None
    salary = None
    role = None 
    if "Name" in employee_info:
        name = employee_info["Name"]
    if "Salary" in employee_info:
        salary = employee_info["Salary"]
    if "Role" in employee_info:
        role = employee_info["Role"]
    print("Name:", name)
    print("Salary:", salary)
    print("Role:", role)
    remaining = dict(employee_info)
    if "Name" in remaining:
        del remaining["Name"]
    if "Salary" in remaining:
        del remaining["Salary"]
    if "Role" in remaining:
        del remaining["Role"]
    if len(remaining) == 0:
        print("No other info!")
    else:
        for key in remaining:
            print(key + ":", remaining[key])
