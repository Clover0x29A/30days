e_name = input("What is the employee's name? ")
e_hourly = input("How much does the employee make an hour? ")
e_hours_worked = input("How many hours did the employee work? ")
e_hourly = float(e_hourly)
e_hours_worked = float(e_hours_worked)
e_name = e_name.title()
print(f"{e_name} worked {e_hours_worked} for a total of ${e_hours_worked * e_hourly}")