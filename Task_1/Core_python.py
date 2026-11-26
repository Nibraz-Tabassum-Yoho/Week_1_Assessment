class InvalidSalaryError(Exception):
    pass

# Requirement 1
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if 'cap' in options:
        result = min(result, options['cap'])
    return result

print(bonus(30000))
print(bonus(30000, 0.2, 1000, 2000))
print(bonus(60000, 0.1, 1000, 2000, cap=5000))

# Requirement 2

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary,{salary}")
        self.name = name
        self.salary = salary
        

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (f"Name: {self.name}, Salary: {self.salary}, "
                f"Team Size: {self.team_size}")


emp = Employee("Arun", 30000)
mgr = Manager("Priya", 45000, 5)

print(emp.get_details())
print("Annual Salary:", emp.annual_salary())

print(mgr.get_details())
print("Annual Salary:", mgr.annual_salary())

# Requirement 3

try:
    emp = Employee("Arun", -30000)
    print("Name:", emp.name)
    print("Annual Salary:", emp.annual_salary())

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")


# Requirement 4

employees = [
    (1, "Arun", "Sales", 30000, "Chennai"),
    (2, "Priya", "HR", 45000, "Chennai"),
    (3, "Rahul", "IT", 60000, "Bangalore"),
    (4, "Divya", "IT", 75000, "Chennai"),
    (5, "Karthik", "Finance", 90000, "Mumbai"),
    (6, "Meena", "Sales", 52000, "Bangalore"),
    (7, "Suresh", "IT", 68000, "Chennai"),
    (8, "Anitha", "HR", 48000, "Mumbai")
]

names = [emp[1] for emp in employees if emp[3] > 50000]
print("Above 50000:", names)

chennai = list(filter(lambda emp: emp[4] == "Chennai", employees))
chennai_names = [emp[1] for emp in chennai]
print("Chennai:", chennai_names)

raised_salary = list(map(lambda emp: round(emp[3] * 1.10,2),employees))
print("Salary after 10% raise:",raised_salary)


# Requirement 5

for emp in employees:

    if emp[3] == 0:
        continue

    if emp[3] > 85000:
        break

    print(emp[1], emp[3])