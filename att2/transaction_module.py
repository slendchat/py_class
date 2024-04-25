import datetime

def is_valid_date(date_str):
  try:
    date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    if date >= datetime.datetime(2024,1,1) and date <= datetime.datetime.now():
      return True
  except:
    return False

def is_valid_time(time_str):
  try:
    datetime.datetime.strptime(time_str, "%H:%M")
    return True
  except:
    return False

def write_transaction(file_path, date, time, amount, operation_type):
  try:
    operation_type = "income" if operation_type == "+" else "expense" if operation_type == "-" else None
    with open(file_path, "a") as file:
      file.write("{} {} {} {}\n".format(date, time, amount, operation_type))
  except:
    print('Error writing to file')
  return


def calculate_balance(file_path):
  balance = 0
  try:
    with open(file_path, "r") as file:
      for line in file:
        line_splitted = line.split()
        amount = float(line_splitted[2])
        operation_type = line_splitted[3]
        if operation_type == "income":
          balance += amount
        elif operation_type == "expense":
          balance -= amount
  except:
    print("Error reading from file")
  return balance

def find_most_profitable_transaction(file_path):
  max_profit = float("-inf")
  res = "none"
  try:
    with open(file_path, "r") as file:
      for line in file:
        line_splitted = line.split()

        if line_splitted[3] != "income":
          continue
        
        amount = float(line_splitted[2])
        if amount > max_profit:
          max_profit = amount
          res = line
  except:
    print("Error reading from file")
  return res


def find_most_unprofitable_transaction(file_path):
  max_expense = float("-inf")
  res = "none"
  try:
    with open(file_path, "r") as file:
      for line in file:
        line_splitted = line.split()

        if line_splitted[3] != "expense":
          continue
        
        amount = float(line_splitted[2])
        if amount > max_expense:
          max_expense = amount
          res = line
  except:
    print("Error reading from file")
  return res



