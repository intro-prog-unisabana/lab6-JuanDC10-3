# Write your code here!
def employee_print(employee_info):
    Name = None
    Salary = None
    Rol = None
    if "Name" in employee_info:
        Name = employee_info["Name"]
    if "Salary" in employee_info:
        Salary = employee_info["Salary"]
    if "Rol" in employee_info:
        Rol = employee_info["Rol"]
    print("Name:", Name)
    print("Salary:", Salary)
    print("Rol:", Rol)
    