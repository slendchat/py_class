from transaction_module import *


# MAIN MENU

file_path = "transactions.txt"

while True:
    print("1) Write transaction data to file")
    print("2) Display current balance")
    print("3) Display data about the most profitable transaction")
    print("4) Display data about the most unprofitable transaction")
    print("5) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter transaction date (dd.mm.yyyy): ")
        if not is_valid_date(date):
          print("Not valid date")
          continue
        time = input("Enter transaction time (hh:mm): ")
        if not is_valid_time(time):
          print("Not valid time")
          continue
        amount = input("Enter transaction amount: ")
        operation_type = input("Enter transaction type (income type +  expense type -): ")
        if not operation_type in ["+","-"]:
          print("Not valid operation type")
          continue
        write_transaction(file_path, date, time, amount, operation_type)
    elif choice == "2":
        balance = calculate_balance(file_path)
        print("Current balance: {}".format(balance))
    elif choice == "3":
        transaction_income = find_most_profitable_transaction(file_path)
        print("Most profitable transaction: {}".format(transaction_income))
    elif choice == "4":
        transaction_expence = find_most_unprofitable_transaction(file_path)
        print("Most unprofitable transaction: {}".format(transaction_expence))
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")