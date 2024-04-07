import re

# REQUIRED GLOBALS
data_file = open("lab05_files/data.txt","w+")

pattern_name = r'^[a-zA-Z]'
pattern_dep = r'^[a-zA-Z0-9]'

# FUNCTIONS 
def input_data():
  surname = input("фамилия: ")
  if(len(surname)<2 or len(surname)>19):
    print("wrong length")
    return
  surname_split = surname.split("-")
  for word in surname_split:
    if not re.match(pattern_name,word):
      print("wrong input")
      return


  name = input("имя: ")
  if(len(name)<2 or len(name)>19):
    print("wrong input")
    return
  name_split = surname.split("-")
  for word in name_split:
    if not re.match(pattern_name,word):
      print("wrong input")
      return
      

  department = input("департмент: ")
  dep_split=department.split(" ")
  if(len(dep_split)>2):
    print("wrong input")
    return
  for word in dep_split:
    if not(re.match(pattern_dep,word)):
      print("wrong input")
      return
    

  kids = input("количество детей: ")
  try:
    number = int(kids)
  except:
    print("not a number")
    return
  if number < 0 or number > 19:
    print("wrong number")
    return
  
  data_file.write(surname + "\t" + name + "\t" + department + "\t" + kids + "\n")

def show_data():
  data_file.seek(0)
  counter_kids = 0
  for line in data_file:
    line_split = line.split("\t")
    kids = line_split[-1].strip("\n")
    print("parent: "+line_split[0]+" "+line_split[1]+" kids: "+kids)
    if(int(kids)>0):
      counter_kids+=int(kids)
  print(f"amount of kids for Santa:{counter_kids}")


def show_no_kids():
  data_file.seek(0)
  parents_no_kids = []
  for line in data_file:
    line_split = line.split("\t")
    kids = line_split[-1].strip("\n")
    if(int(kids)==0):
      parents_no_kids.append(line_split[0]+" "+line_split[1])
  if len(parents_no_kids) == 0:
    print("no such parents")
    return
  print("parents with no kids:")
  for parent in parents_no_kids:
    print(parent)
  return

# MAIN MENU
while(True):
  choice = input("###MENU###\n1 - ввод даных в файл\n2 - просмотр данных о детях сотрудников\n3 - поиск и вывод списка бездетных сотрудников\n4 - выход\n")
  if (choice == "1"):
    input_data()
  elif (choice == "2"):
    show_data()
  elif (choice == "3"):
    show_no_kids()
  elif (choice == "4"):
    break
  else:
    print("wrong input")

data_file.close()