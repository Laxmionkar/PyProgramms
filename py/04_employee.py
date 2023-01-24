class Employee:
    company = "Google"
    salary = 100

kiran = Employee()
rajni = Employee()
kiran.salary = 300
rajni.salary = 400

print(kiran.company)
print(rajni.company)
Employee.company = "YouTube"
print(kiran.company)
print(rajni.company)
print(kiran.salary)
print(rajni.salary)
