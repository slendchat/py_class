num_list = [52,69,1488,228,1337]

print("el1:",num_list[0])
print("el3:",num_list[2])

print(num_list[::])

print("el2:",num_list[1])
num_list[1]=808005535
print("el2:",num_list[1])

num_list.append(42)
num_list.insert(1,777)
print("append and insert:\n",num_list[::])
num_list.pop(0)
print("pop:\n",num_list[::])
print("len of list: ", len(num_list))
print("min: ",min(num_list)," max: ",max(num_list))

data = ("spb",-52,"vanya belyi","dead_goose",228)
print("type of tuple:\n",type(data))
print(data[0])
print(data[-1])
print(data[::])
print("size: ", len(data))
print("abs: ", abs(data[1]))
print("bin: ", bin(data[-1]))


myset = {"alpha","sigma","beta","alpha"}
print(myset)
myset.add("epsilon")
print(myset)
myset.discard("epsilon")
print(myset)
print(len(myset))
myset.clear()

dict_str = {"a":1,"b":2,"c":3}
dict_num = {1:"a",2:"b",3:"c"}
print(dict_str["a"],dict_str["b"])
print(dict_num[1],dict_num[2])
print(dict_num.get(3,"aboba"))
dict_str.pop("a")
dict_str["b"]=pow(dict_str["b"],2)
print(type(dict_str["c"]))
dict_str.update(dict_num)
print(dict_str)
print(dict_str.keys())

num_tuple=tuple(num_list)
print(type(num_tuple))
data_set = set(data)
print(type(data_set))

newdict={}
for i in range(len(num_list)):
  newdict[f"{i}"] = num_list[i];
print(newdict)


#TASK2

list_num2 = [9995,9610,44795]
list_str2 = ["used 2007 Mitsubishi Eclipse GS Spyder Sportronic","used Toyota Celica GT","2024 Civic Type R"]

my_str = "Car:{3}\nPrice:{0}$\nOr you can buy:{4}\n for {1}$\nfinally {5}\n For {2}$ XD".format(list_num2[0],list_num2[1],list_num2[2],list_str2[0],list_str2[1],list_str2[2])
print(my_str)

age = int(input("enter how old u are: "))
print(f"smoking halfes your life. If you weren`t smoking you could be {age*2} "+", see u looser?")

if list_str2[2] in my_str:
  print("STRING IS IN MY_STR")

chars = "qwertyuiopasdfghjklzxcvbnm"

for ch in chars:
  if ch not in "aeoui":
    print(f"not a vowel [{ch}]")
