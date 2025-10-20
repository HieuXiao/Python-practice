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
print(list)
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

# ===Counting lists===
from random import random as rnd

mylist = []
for i in range(20):
    mylist.append(int(rnd() * 10))
print('\nRandom list: ', mylist)
for i in range(10):
    print("frequency of {}: {}".format(i, mylist.count(i)))

# === Tuple ===
mytuple1 = 5, 7, "name", 8
mytuple2 = (5, 7, "name", 8)
print("Fist tuple: ", mytuple1)
print("Second tuple: ", mytuple2)

a1 = (1212, "First St", "SF", "CA")
a2 = (2323, "Second St", "Seattle", "WA")
a3 = (3434, "Third St", "Denver", "CO")
Addresses = []
Addresses.append(a1)
Addresses.append(a2)
Addresses.append(a3)
print('\nAddresses: ', Addresses)
print('Designated address: ', Addresses[1][1])

# === Dictionaries ===
CA = {
    "name": "California",
    "capital": "Sacramento",
    "areakm2": 423970,
    "population": 39538223
}
print('\nCA len: ', len(CA))
print('CA: ', CA)

GROVELAND = {"ELEVATION": 853,
             "LATITUDE": 37.8444,
             "LONGITUDE": -120.2258,
             "PRECIPITATION": 176.02
             }
print('\nGROVELAND len: ', len(GROVELAND))
print('GROVELAND: ', GROVELAND)

PRECIPITATION = {"GROVELAND": 176.02,
                 "LEE VINING": 71.88,
                 "PLACERVILLE": 170.69}
print('\n', PRECIPITATION["PLACERVILLE"])
print('Origin precipitation: ', PRECIPITATION)
PRECIPITATION["BRIDGEPORT"] = 41.4
print('After change preciptation: ', PRECIPITATION)

print("\n----PRECIPITATION----")
PRECIPITATION.keys()
for station in PRECIPITATION.keys():
    print(PRECIPITATION[station])
print(PRECIPITATION.keys())
print(GROVELAND.keys())

'''
==================1.3 Mathematical Computation Using Operators=================================
'''
# ========= Arithmetic operators ============
print('\n========= Arithmetic operators ============')
x = 2 + 3
y = 2. + 3
z = 2 - 3
print('Check type:', type(x), ' - ', type(y), ' - ', type(z))

m = 2 * 3
print('\nResult: ', m)
print('Type: ', type(m))

print('\nDivide')
print(1 / 2)
print(1. / 2)
print(4 / 2)

print('\n=== Power ===')
print(5 ** 2)
print(5 ** 2.0)

print('\n=== Square root ===')
print(25 ** (1 / 2))
print(25 ** 0.5)

print('\n=== Modulo ===')
print("modulus = 10")
for n in range(2, 14, 2):
    print(n, n % 10)  # 10 might be a common repeated value
print("modulus = 360, for compass azimuth (°)")
for n in range(90, 720, 90):
    print(n, n % 360)  # Compass azimuth (°) is a good application of modulos in a cycle.15

# =================== Conversion functions ====================
print('\n=================== Conversion functions ====================')
print(type(5.23))
print(type(str(5.278)))  #Converts a number to a string.
print(type( int("4") ))
print(type( int(float("4.17")) ))
# ❌ int("4.17") - lỗi vì "4.17" không phải chuỗi biểu diễn số nguyên hợp lệ

