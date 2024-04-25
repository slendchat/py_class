import datetime
import re


class Employee:
  def __init__(self, name="", phone="", bday="", email="", position=""):
    self.__name = name
    self.__phone = phone
    self.__bday = bday
    self.__email = email
    self.__position = position
  
  def calculate_age(self):
    today = datetime.date.today() 
    bday = datetime.date(int(self.__bday[6:10]), int(self.__bday[3:5]), int(self.__bday[0:2])) # year month day #08.03.2004
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))                         #0123456789
    return age

  def _calculate_salary(self):
    pass
  
  def show_info(self):
    print("name: {}".format(self.__name))
    print("phone: {}".format(self.__phone))
    print("bday: {}".format(self.__bday))
    print("email: {}".format(self.__email))
    print("position: {}".format(self.__position))
    print("age: {}".format(self.calculate_age()))

# GETTERS SETTERS

  def get_name(self):
    return self.__name

  def set_name(self, value):
    self.__name = value

  name = property(get_name, set_name)

  def get_phone(self):
    return self.__phone

  def set_phone(self, value):
    self.__phone = value

  phone = property(get_phone, set_phone)

  def get_bday(self):
    return self.__bday

  def set_bday(self, value):
    self.__bday = value

  bday = property(get_bday, set_bday)

  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, value):
    self.__email = value

  @property
  def position(self):
    return self.__position
  
  @position.setter
  def position(self, value):
    self.__position = value
# END OF CLASS


class Hourly_employee(Employee):
  def __init__(self, name="", phone="", bday="", email="", position="", hourly_rate=0, hours_worked=0):
    super().__init__(name, phone, bday, email, position)
    self.__hourly_rate = int(hourly_rate)
    self.__hours_worked = int(hours_worked)

  @property
  def hourly_rate(self):
    return self.__hourly_rate
  @hourly_rate.setter
  def hourly_rate(self, value):
    self.__hourly_rate = int(value)

  @property
  def hours_worked(self):
    return self.__hours_worked
  @hours_worked.setter
  def hours_worked(self, value):
    self.__hours_worked = int(value)
    
  def _calculate_salary(self):
    return self.__hourly_rate * self.__hours_worked

class Salary_employee(Employee):
  def __init__(self, name="", phone="", bday="", email="", position="", salary=0):
    super().__init__(name, phone, bday, email, position)
    self.__salary = int(salary)

  @property
  def salary(self):
    return self.__salary
  @salary.setter
  def salary(self, value):
    self.__salary = int(value)

  def _calculate_salary(self):
    return self.__salary  
