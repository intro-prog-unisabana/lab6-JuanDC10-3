# Write your code here!
def employee_print(employee_info):
    name = None
    salary = None
    rol = None
    if "Name" in employee_info:
        name = employee_info["Name"]
    if "Salary" in employee_info:
        salary = employee_info["Salary"]
    if "Rol" in employee_info:
        rol = employee_info["Rol"]
    print("Name:", name)
    print("Salary:", salary)
    print("Rol:", rol)
