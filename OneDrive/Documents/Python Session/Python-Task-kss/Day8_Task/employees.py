file = open("employees.txt", "r")

high_name = ""
high_salary = 0

print("Employee Details:")

for line in file:
    print(line.strip())
    data = line.split()

    if int(data[1]) > high_salary:
        high_salary = int(data[1])
        high_name = data[0]

file.close()

print("Highest Salary Employee =", high_name)
print("Salary =", high_salary)

file = open("employees.txt", "a")

name = input("Enter employee name: ")
salary = input("Enter salary: ")

file.write(name + " " + salary + "\n")
file.close()

print("New employee record added.")
