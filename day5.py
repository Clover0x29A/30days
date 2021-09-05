num1 = 1
num2 = 2
id1 = id(num1)
id2 = id(num2)

if id1 == id2:
    print("numbers are the same.")
else:
    print("numbers are not equal.")

numbers = [1, 2, 3, 4]
id1 = id(numbers)
new_numbers = numbers + [5]
id2 = id(new_numbers)

print(f"{id1}, {id2}")

id1 = id(numbers)

numbers.append(5)
id2 = id(numbers)
print(f"{id1}, {id2}")

number_input = int(input("enter a number: "))

if number_input < 0:
    print("Number is negative.")
elif number_input == 0:
    print("Number is 0.")
else:
    print("Number is positive.")

wage = float(input("How much does the employee make an hour? "))
hours = float(input("How many hours did the employee work? "))

if hours > 40:
    pay = wage * 40
    hours -= 40
    wage_overtime = (wage * 0.1) + wage
    pay += wage_overtime * hours
    print(f"Employee made ${pay}")
else:
    print(f"Employee made ${hours * wage}")