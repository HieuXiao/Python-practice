'''
1.1 PYTHON VARIABLES
'''
# ===Numeric variable===
x = -17
print(type(x))
x = -23.568
print(type(x))
print('\n')

#  ===String variables (made of text)===
path = "c:/prog/mydata"
print(path)
print('\n')

# === Boolean variables (true or false)===
tf = 5 > 6
print(tf)
print(type(tf))
print(type(True))
print('\n')

# === Functions, methods and properties===
import math

sin = math.sin
radians = math.radians
pi = math.pi
print(abs(-5))
print(sin(30 / 180 * pi))
print(sin(radians(30)))
print('\n')

'''
1.2 Lists, Tuples, and Dictionaries
'''
# ===List===
x = 5
msg = "Hello"
path = "c:/py/data"
aList = [5, 7.83, "Fred"]
list = [x, msg, path, 2.7, aList]
print (list)
print(list[0])
print(list[0:3])

print(list[-2:])

print(list[1:2])
print(list[1:2][0])
print(list[1]==list[1:2][0])
print('\n')
a1 = [1212, "First St", "SF", "CA"]
a2 = [2323, "Second St", "Seattle", "WA"]
a3 = [3434, "Third St", "Denver", "CO"]
Addresses = []
Addresses.append(a1)
Addresses.append(a2)
Addresses.append(a3)
print(Addresses[0])
print(Addresses[1][1])
print(Addresses[2][3])
print("\n")


# ===append vs extend===
Pacific = ['AK', 'CA', 'OR', 'WA']
Desert = ['AZ', 'NV', 'UT']
Mountain = ['ID', 'MT', 'WY', 'CO', 'NM']
WestStates = Pacific + Desert + Mountain
print(WestStates)

States = Pacific
States.append(Desert)
print(States)

# ===Sorting lists===
from random import random as rnd

mylist = []
for i in range(20):
    mylist.append(int(rnd() * 10))
print(mylist)
mylist.sort()
print(mylist)