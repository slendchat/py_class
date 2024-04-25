#TASK 1
#3
name = input("write ur name:")
print("hi",name,"!!!")

#4
print("\n\n")
var1_int = int(1)
var2_float = float(2.0)
var3_str = str("short str")
var4_longstr = '''this is my huge
str made by me
idk what to write else'''

#5
print("\n\n")
print(type(var1_int))
print(type(var2_float))

#6
print("\n\n")
print(len(var3_str))

#7
print("\n\n")
print(var4_longstr.upper())

#8
print("\n\n")
buf = var3_str[2:5]
print(buf)
print("\n\n")

#TASK 2
#a)
txt = "More results from text..."
substr = txt[4:12]
print(substr)                         # results
print(substr.strip())                 #results

"""
strip method removes spaces in the
beggining and in the end of string
you also can specify which characters to remove
for example string str="**-+*branza*=**!"
str.strip("*-+=!") will result str = "branza" 
"""


#b) 
txt = "More results from text..."
print(txt.split())                    #['More', 'results', 'from', 'text...']

"""
split method will split the string into list 
by adding to list words separated by whitespaces by default
but u can specify ur own separator and maxsplit
str.split(",",1) will split string only one time when ',' occured
"""

#c)
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))                #My name is Mary, and I am 36
"""
inserts specified value into string
"""
