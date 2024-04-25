from lab06_module import *

#patterns
name_pattern = r'^[a-zA-Z]{,254}$'
phone_pattern = r'^\+373\d{8}$'
bday_pattern = r'^(0[1-9]|[1-2][0-9]|3[0-1])\.(0[0-9]|1[0-2])\.(19[6-9]\d|200[0-7])$'
email_pattern = r'^[a-zA-Z\d]{2,20}([.-_][a-zA-Z\d]{2,20})*@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$'
position_pattern = r'^[a-zA-Z]{4,20}$'


def create_employee(emp):

  name = input("name: ")
  if not re.match(name_pattern, name):
    raise Exception("wrong {}".format(name))
  phone = input("phone: ")
  if not re.match(phone_pattern, phone):
    raise Exception("wrong {}".format(phone))
  bday = input("bday: ")
  if not re.match(bday_pattern, bday):
    raise Exception("wrong {}".format(bday))
  email = input("email: ")
  if not re.match(email_pattern, email):
    raise Exception("wrong {}".format(email))
  position = input("position: ")
  if not re.match(position_pattern, position):
    raise Exception("wrong {}".format(position))
  
  emp.name = name
  emp.phone = phone
  emp.bday = bday
  emp.email = email
  emp.position = position

def create_salary_employee(emp):
  create_employee(emp)
  salary = input("salary: ")
  emp.salary = salary

def create_hourly_employee(emp):
  create_employee(emp)
  hourly_rate = input("hourly_rate: ")
  hours_worked = input("hours_worked: ")
  emp.hourly_rate = hourly_rate
  emp.hours_worked = hours_worked

# MAIN

emp1 = Employee()
emp2 = Employee()

emp_s1 = Salary_employee()
emp_s2 = Salary_employee()

emp_h1 = Hourly_employee()
emp_h2 = Hourly_employee()

print("first employee")
create_employee(emp1)
emp1.show_info()
print("second employee")
create_employee(emp2)
emp2.show_info()

print("first salary employee")
create_salary_employee(emp_s1)
emp_s1.show_info()
print("salary: "+emp_s1._calculate_salary())
print("second salary employee")
create_salary_employee(emp_s2)
emp_s2.show_info()
print("salary: "+emp_s2._calculate_salary())

print("first hourly employee")
create_hourly_employee(emp_h1)
emp_h1.show_info()
print("salary: {}".format(emp_h1._calculate_salary()))
print("second hourly employee")
create_hourly_employee(emp_h2)
emp_h2.show_info()
print("salary: {}".format(emp_h2._calculate_salary()))








