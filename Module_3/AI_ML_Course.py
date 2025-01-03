#!/usr/bin/env python
# coding: utf-8

# ### Variables

# In[ ]:


# possible variables
name, name1, name_1, Name, 

# Non variables
1name, 1.name, name.1 


# In[3]:


firstName = "john" # camel case
last_name = "Doe" # snake case


# ### Datatypes

# In[4]:


number = 12
decimal_number = 3.14
string = "apple"
boolean = True # False


# In[7]:


type(number), type(decimal_number), type(string), type(boolean)


# In[8]:


type("12345")


# ### Typecast

# In[11]:


num = 12
num2 = str(num)
num2, type(num2), type(num)


# In[13]:


num2, int(num2), float(num2)


# In[14]:


int(string)


# ### Print function

# In[15]:


print("hello world!!!")


# In[16]:


print(string)


# In[17]:


print(strings)


# In[18]:


print(12345)


# In[19]:


print(12.45)


# In[23]:


print(type(number), type(decimal_number), type(string), type(boolean), sep="\n")


# In[24]:


# I bought 3 kgs of apple for 148.35Rs
weight = 3
fruit = "apple"
cost = 148.35


# In[31]:


# method-1 (using comma)
print("I bought",weight,"kgs of",fruit,"for",cost,"Rs")

# method-2 (using typecast)
print("I bought "+str(weight)+" kgs of "+fruit+" for "+str(cost)+"Rs")

# method-3
print("I bought %d kgs of %s for %0.2fRs"%(weight, fruit, cost))

# method-4
print(f"I bought {weight} kgs of {fruit} for {cost}Rs")


# ### input Functions

# In[32]:


randomNumber = input()


# In[35]:


firstName = input("Enter your first name: ")


# In[36]:


print(firstName)


# In[37]:


phone_number = input("Enter your 10 digit phone number: ")


# In[39]:


type(phone_number)


# ### Operators

# #### Arithmetic Operators

# In[40]:


# + - * / % // **
print(8 + 5)
print(8 - 5)
print(8 * 5)
print(8 / 5)
print(8 % 5)
print(8 // 5)
print(8 ** 5)


# In[42]:


# + *
print("butter" + "jam")
print("apple" * 3)


# #### Comparison Operators

# In[43]:


# > >= < <= == !=

print(8 > 5)
print(8 >= 5)
print(8 < 5)
print(8 <= 5)
print(8 == 5)
print(8 != 5)


# #### logical Operators

# In[44]:


# and or not

print(8 > 5 and 3 < 10)
print(8 > 5 and 13 < 10)
print(8 > 15 and 13 < 10)

print(8 > 5 or 3 < 10)
print(8 > 5 or 13 < 10)
print(8 > 15 or 13 < 10)

num = None
print(not num)

num = 10
print(not num)


# ### Conditional Statements

# In[ ]:


if condition :
    "statement"
    "statement2"
else:
     "statement"


# In[46]:


num = int(input("Enter any number :"))
if num % 2 == 0:
    print("the given number is even")
else:
    print("the given number is odd")


# In[49]:


num = int(input("Enter any number :"))
output = "the given number is odd"
if num % 2 == 0:
    output = "the given number is even"
print(output)


# In[52]:


num = int(input("Enter any number :"))
if num % 4 == 0:
    print("the given number is divisible by 4 and even")
elif num % 2 == 0:
    print("the given number is even")
else:
    print("the given number is odd")


# In[58]:


num = int(input("Enter any number :"))
if num % 2 == 0:
    output = "the given number is even"
    if num % 4 == 0:
        output = "the given number is divisible by 4 and also even"
    print(output)
else:
    print("the given number is odd")


# ### While loop

# In[ ]:


while condition:
    statements


# In[59]:


count = 1
while count <= 3:
    num = int(input("Enter any number :"))
    if num % 4 == 0:
        print("the given number is divisible by 4 and even")
    elif num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")
    
    count += 1


# In[60]:


option = "y"
while option == "y":
    num = int(input("Enter any number :"))
    if num % 4 == 0:
        print("the given number is divisible by 4 and even")
    elif num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")
    
    option = input("Do you want to continue? y/n: ")


# In[61]:


while True:
    num = int(input("Enter any number :"))
    if num % 4 == 0:
        print("the given number is divisible by 4 and even")
    elif num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")


# In[63]:


while True:
    num = int(input("Enter any number :"))
    
    if num == 15:
        print("Stopping....")
        break
    elif num == 25:
        print("Skipping....")
        continue
        
    if num % 4 == 0:
        print("the given number is divisible by 4 and even")
    elif num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")


# In[80]:


# write a python program for calculating of 3 objects, the object has to be selected

print(
    "This program can calculate the area of three objects. Please select one")
print("1. Circle")
print("2. Rectangle")
print("3. triangle")
while True:
    choice = input("Enter your choice: ")

    if choice == "circle" or choice == "1":
        r = float(input("Enter the radius of the circle: "))
        area = 3.14 * r * r
        print("Area of the circle is", area)

    elif choice == "rectangle" or choice == "2":
        l = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the breadth of the rectangle: "))
        area = l * b
        print("Area of the rectangle is", area)

    elif choice == "triangle" or choice == "3":
        b = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = b * h * 0.5
        print("Area of the rectangle is", area)

    else:
        print("Invalid option. Please select proper option")
        continue
    
    option = input("Do you want to continue? y/n:")
    if option != "y":
        break
else:
    print("Good bye...")


# ### For loops

# In[65]:


for i in range(5):
    print(i)


# In[66]:


for i in range(5):
    print("hello")


# In[68]:


for _ in range(3):
    num = int(input("Enter any number :"))
    if num % 4 == 0:
        print("the given number is divisible by 4 and even")
    elif num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")


# In[70]:


for i in range(16, 21):
    print(i)


# In[72]:


for i in range(1,10,2):
    print(i)


# In[73]:


for i in firstName:
    print(i)


# In[75]:


for i,j in zip(firstName, last_name):
    print(i,j)


# In[77]:


for i, char in enumerate(firstName):
    print(i, char)


# In[79]:


for _ in range(3):
    num = int(input("Enter any number :"))
    if num % 4 == 0:
        print("the given number is divisible by 4 and even")
    elif num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")
else:
    print("Thank you!!!")


# In[84]:


# identifying prime numbers between two numbers

for num in range(0, 21):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


# ### Example - Rock paper scissor Game

# Write a program for rock-paper-scissor game using the following rules, Game should be executed until any of the players wants to quit.
# 
# * Rock beats Scissor
# * Scissor beats Paper
# * Paper beats Rock

# In[86]:


while True:
    player1 = input("Enter your player-1 :")
    if player1 == "quit" or player1 == "q":
        print("Good Bye....")
        break

    player2 = input("Enter your player-2 :")
    if player2 == "quit" or player2 == "q":
        print("Good Bye....")
        break

    print("player_1 choice is ", player1, "and player_2 choice is ", player2)

    if player1 == player2:
        print("Game is tie")
        continue
    elif player1 == "rock" and player2 == "scissor":
        print("player_1 won the game")
    elif player1 == "scissor" and player2 == "paper":
        print("player_1 won the game")
    elif player1 == "paper" and player2 == "rock":
        print("player_1 won the game")
    else:
        print("player_2 won the game")
    print()


# ### String Operations

# In[87]:


animal = "elephant"
sentence = "elephant is an animal"


# #### Slice and dice

# In[89]:


animal[5]


# In[90]:


len(animal)


# In[92]:


animal[3:]


# In[93]:


animal[:5]


# In[94]:


animal[2:6]


# In[96]:


animal[1:6], animal[1:6:2]


# In[97]:


animal[::-1]


# #### String function

# In[103]:


# case
animal.capitalize(), sentence.capitalize()
animal.upper(), sentence.upper()
animal.lower(), sentence.lower()
animal.title(), sentence.title()
"ElEpHaNt".swapcase()
"ElEpHaNt".casefold()


# In[107]:


# decorative 
animal.center(40,"~")
animal.zfill(15)


# In[111]:


# slice and join
sentence.split()
splittedSentence = sentence.split('an')
splittedSentence


# In[115]:


"an".join(splittedSentence)


# In[117]:


animal.count('e'), sentence.count('an')


# In[119]:


animal.replace("l","Y")


# In[123]:


animal.endswith("nt"), animal.startswith('el')


# In[126]:


sentence.encode('utf16').decode('utf16')


# In[127]:


sentence.find('an'), sentence.index('an')


# In[128]:


sentence[5:7]


# In[129]:


animal.find('y')


# In[130]:


animal.index('y')


# In[132]:


animal.isupper(), animal.islower()


# In[134]:


animal.isalnum(), animal.isalpha()


# In[135]:


"1234".isalpha()


# In[ ]:


animal.is


# ### List

# In[136]:


emptyList = []


# In[137]:


print(emptyList)


# In[138]:


contentList = ["apple","mango","pineapple", "orange", 12,45,26,3.14]


# In[139]:


print(contentList)


# #### Slice and Dice

# In[140]:


contentList[2]


# In[141]:


contentList[2][4]


# In[142]:


len(contentList)


# In[143]:


contentList[2:6]


# In[144]:


contentList[2:]


# In[145]:


contentList[:6]


# In[146]:


# CRUD 
contentList[7]


# In[147]:


contentList[7] = 5.18


# In[148]:


contentList


# In[149]:


del contentList[6]


# In[150]:


contentList


# #### List functions

# In[151]:


emptyList.append("new")


# In[152]:


emptyList


# In[153]:


contentList.append("papaya")


# In[154]:


contentList


# In[155]:


contentList.insert(5, "carrot")


# In[156]:


contentList


# In[157]:


contentList.pop()


# In[158]:


contentList


# In[159]:


contentList.remove(12)


# In[160]:


contentList


# In[161]:


contentList.count("apple")


# In[162]:


contentList.index("orange")


# In[163]:


newList = contentList


# In[165]:


newList.pop()


# In[166]:


newList


# In[167]:


contentList


# In[168]:


newlist2 = contentList.copy()


# In[170]:


newlist2.pop()


# In[171]:


newlist2


# In[172]:


contentList


# In[174]:


emptyList.extend(newlist2)


# In[175]:


emptyList


# In[176]:


emptyList[::-1]


# In[179]:


emptyList.reverse()


# In[180]:


emptyList


# In[182]:


contentList.sort()


# In[183]:


emptyList.sort()


# In[185]:


emptyList.sort(reverse=True)


# In[186]:


emptyList


# ### Tuples

# In[187]:


emptyTuple = ()


# In[188]:


contentTuple = ('pineapple', 'orange', 'new', 'mango', 'carrot', 'apple')


# In[189]:


contentTuple[3:]


# In[190]:


contentTuple[3:7]


# In[192]:


contentTuple[4] = "beetroot"


# In[193]:


del contentTuple[4]


# In[194]:


a,b,c = (3,6,9)


# In[196]:


a


# ### Dictionary

# In[197]:


emptyDict = {}


# In[198]:


contentDict = {
    "a": "apple",
    "b": "banana",
    12: "carrot",
    4.5: "papaya",
    "tuple": contentTuple,
    "list": contentList
    
}


# In[199]:


contentDict


# In[200]:


contentDict['b']


# In[201]:


contentDict['b'] = "bat"


# In[202]:


contentDict


# In[203]:


del contentDict['b']


# In[204]:


contentDict


# In[205]:


contentDict['b'] = "banana"


# In[206]:


contentDict['b']


# In[207]:


contentDict


# #### Dictionary methods

# In[208]:


contentDict.keys()


# In[209]:


contentDict.values()


# In[210]:


contentDict.items()


# In[211]:


contentDict.pop("b")


# In[212]:


contentDict


# In[213]:


contentDict.popitem()


# In[215]:


emptyDict.update(contentDict)


# In[216]:


emptyDict


# ### looping over data structures

# In[217]:


for ele in contentList:
    print(ele)


# In[218]:


for ele1,ele2 in zip(contentList, newlist2):
    print(ele1, ele2)


# In[219]:


for ele in contentTuple:
    print(ele)


# In[222]:


for ele in contentDict:
    print(ele)


# In[221]:


for ele in contentDict.values():
    print(ele)


# In[224]:


for k,v in contentDict.items():
    print(k,"-->", v)


# In[225]:


for i in range(len(contentList)):
    print(contentList[i])


# #### Example of Dictionary and list looping

# In[226]:


students = [
    {
        "name": "Alice Johnson",
        "age": 14,
        "subjects": {
            "Math": 85,
            "Science": 90,
            "English": 88
        }
    },
    {
        "name": "Bob Smith",
        "age": 15,
        "subjects": {
            "Math": 78,
            "Science": 83,
            "English": 75
        }
    },
    {
        "name": "Charlie Brown",
        "age": 14,
        "subjects": {
            "Math": 92,
            "Science": 89,
            "English": 94
        }
    },
    {
        "name": "David Wilson",
        "age": 15,
        "subjects": {
            "Math": 74,
            "Science": 80,
            "English": 72
        }
    },
    {
        "name": "Emma Davis",
        "age": 14,
        "subjects": {
            "Math": 88,
            "Science": 92,
            "English": 91
        }
    }
]


# In[229]:


students[0]['subjects']['Math']


# In[232]:


sum(students[0]['subjects'].values())


# In[237]:


for obj in students:
    if obj['subjects']['Math'] >= 85:
        print(f"Student Name is {obj['name']} and the math mark is {obj['subjects']['Math']}")
        print(f"And the total mark is {sum(obj['subjects'].values())}")
        print()
                                           


# In[238]:


for obj in students:
    if obj['subjects']['Math'] >= 85:
        print(f"Student Name is {obj['name']} and the math mark is {obj['subjects']['Math']}")
        print(f"And the total mark is {sum(obj['subjects'].values())}")
        obj['Total'] = sum(obj['subjects'].values())
        print()
                                           


# In[239]:


students


# ### Sets

# In[240]:


fruits = {"apple", "banana", "pineapple"}


# In[241]:


print(fruits)


# In[242]:


set([1,2,2,3,4,4,5])


# In[244]:


emptySet = set()


# In[245]:


fruits.add("orange")


# In[246]:


fruits.update(["kiwi", ])


# In[247]:


fruits


# In[248]:


fruits.remove('banana')


# In[249]:


fruits


# In[250]:


fruits.remove('banana')


# In[251]:


fruits.discard('banana')


# In[252]:


fruits.discard('kiwi')


# In[254]:


fruits.update(["kiwi", 'banana', 'mango'])


# In[257]:


fruits.pop()


# In[258]:


# union
a = {1,2,3}
b = {3,4,5}


# In[259]:


a.union(b)


# In[260]:


a | b


# In[261]:


# intersection
a.intersection(b)


# In[262]:


a & b


# In[263]:


# difference
a.difference(b)


# In[264]:


b.difference(a)


# In[265]:


a - b


# In[266]:


b - a 


# In[267]:


a.symmetric_difference(b)


# In[268]:


a ^ b


# In[269]:


small = {1, 2}
big = {1,2,3,4}


# In[270]:


small.issubset(big)


# In[271]:


big.issuperset(small)


# In[272]:


set1 = {1,2,3}
set2 = {4,5,6}


# In[273]:


set1.isdisjoint(set2)


# In[274]:


small.isdisjoint(big)


# In[275]:


copySet = fruits.copy()


# In[276]:


copySet


# In[277]:


copySet.clear()


# In[278]:


copySet


# In[279]:


class_A = {"Alice", "Bob", "Charlie", "David"}
class_B = {"Charlie", "David", "Eve", "Frank"}


# In[281]:


# attending both the class
class_A & class_B


# In[282]:


class_A.intersection(class_B)


# In[283]:


# attending one class
class_A ^ class_B


# In[284]:


class_A.symmetric_difference( class_B)


# In[285]:


class_A | class_B


# In[286]:


class_B.union(class_A)


# ### Example: Cows - Bulls

# * The computer generates a random 3-digit number.
# * The player guesses a 3-digit number.
# * If the player guesses a digit that is correct and in the correct position, it's called a 'Cow.'
# * If the player guesses a digit that's in the number but in the wrong position, it's called a 'Bull.'
# * The goal is to guess the number correctly by receiving feedback about the number of 'Cows' and 'Bulls.'"

# In[287]:


import random as r


# In[292]:


num = str(r.randint(100, 999))


# In[294]:


print(num)


# In[ ]:


user = input("Enter your guess: ")
if user.lower() == "quit" or user.lower =="q":
    print('Good bye..,')
    break


# In[ ]:


if len(user) !=3 or not user.isdigit():
    print('Invalid input! Please enter a 3-digit number.')
    continue


# In[ ]:


cow_bull = [0, 0]
for i in range(len(num)):
    if num[i] == user[i]:
        cow_bull[0] += 1


# In[ ]:


for digit in user:
    if digit in num:
        cow_bull[1] += 1
cow_bull[1] -= cow_bull[0]


# In[ ]:


print(f'Cows: {cow_bull[0]}, Bulls: {cow_bull[1]}')


# In[ ]:


attempt = 0
attempt += 1 


# In[ ]:


if cow_bull[0] == 3:
    print(f'You win after {attempt} attempts!')
    break
else:
    print('Your guess isn’t quite right, try again.')


# In[295]:


attempt = 0
while True:
    user = input("Enter your guess: ")
    if user.lower() == "quit" or user.lower =="q":
        print('Good bye..,')
        break

    if len(user) !=3 or not user.isdigit():
        print('Invalid input! Please enter a 3-digit number.')
        continue
        
    cow_bull = [0, 0]
    # cow value calculation
    for i in range(len(num)):
        if num[i] == user[i]:
            cow_bull[0] += 1
                
    # bull value calculation
    for digit in user:
        if digit in num:
            cow_bull[1] += 1
    cow_bull[1] -= cow_bull[0]

    attempt += 1 
    print(f'Cows: {cow_bull[0]}, Bulls: {cow_bull[1]}')
    
    if cow_bull[0] == 3:
        print(f'You win after {attempt} attempts!')
        break
    else:
        print('Your guess isn’t quite right, try again.')


# ### Functions

# In[42]:


def greet():
    print("Hello, welcome to the python for AI/ML Course!!!")


# In[43]:


greet()


# In[ ]:


def function_name(parameters):
    # code block
    return result


# In[44]:


def greet():
    print("Hello, welcome to the python for AI/ML Course!!!")


# In[45]:


greet()


# In[46]:


def add_numbers(a,b):
    return a+b


# In[47]:


result = add_numbers(4,5)
result


# In[49]:


def multiply_numbers(x,y):
    return x*y


# In[50]:


multiply_numbers(3,7)


# In[51]:


def subtract_numbers(x, y):
    return x - y


# In[52]:


subtract_numbers(7,3)


# In[53]:


subtract_numbers(3,7)


# In[54]:


def display(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


# In[55]:


display("John Doe", 30, "Chennai")


# In[56]:


display(name="John Doe", age=30, city="Chennai")


# In[57]:


display(city="Chennai",name="John Doe", age=30 )


# In[58]:


def greet(name="Guest"):
    print(f"hello {name}!!!!")


# In[59]:


greet("John Doe")


# In[60]:


greet()


# In[61]:


def display(name, age=30, city="Chennai"):
    print(f"{name} is {age} years old and lives in {city}")


# In[64]:


display("John Doe", 28, "Mumbai")


# In[ ]:


*args, **kwargs


# In[65]:


def print_numbers(*args):
    for item in args:
        print(item)


# In[68]:


print_numbers(1)


# In[69]:


print_numbers(10, 20,30)


# In[70]:


def sum_numbers(*args):
    print(sum(args))


# In[71]:


sum_numbers(10,12)


# In[72]:


sum_numbers(10,12,8,29,10)


# In[73]:


def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# In[74]:


display(city="Chennai",name="John Doe", age=30 )


# In[75]:


def display_info(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)


# In[76]:


display_info(1,2,3,4,name="John Doe", age=30)


# In[77]:


def take_order(*items, **details):
    print("Order Details:")
    print("Items ordered:", items)
    for key, value in details.items():
        print(f"{key.title()}: {value}")


# In[78]:


take_order("Pizza", "Burger", "Pasta", table_number=5, waiter="John", payment_method="Credit Card")


# In[82]:


def function_order(x, y, *args, name, age, **kwargs):
    print(x, y)
    print(args)
    print(name, age)
    print(kwargs)


# In[84]:


function_order(1,2,4,5,6,name="John Doe", age=35, city="chennai", mobile_no=123456789)


# ### Lambda functions

# In[ ]:


lambda arguments: expression


# In[85]:


def add(x,y):
    return x + y

result = add(3,6)
result


# In[86]:


add = lambda x,y : x + y


# In[87]:


result = add(3,6)
result


# In[88]:


square = lambda x : x ** 2


# In[89]:


square(4)


# In[90]:


multiply = lambda x, y : x * y


# In[91]:


multiply(2,4)


# In[93]:


numbers = [1,2,3,4,5,6, 2 , 4, 7]
square = list(map(lambda x : x ** 2, numbers))
square


# In[94]:


list(filter(lambda x : x % 2 == 0, numbers))


# In[95]:


from functools import  reduce


# In[97]:


reduce(lambda x,y : x * y, numbers)


# In[98]:


def incrementor(n):
    return lambda x:x+n


# In[99]:


inc = incrementor(5)


# In[101]:


inc(7)


# In[102]:


points = [(1,2),(3,1),(5,-1)]


# In[103]:


sorted(points, key=lambda x:x[1])


# ### List Comprehension

# In[ ]:


[expression for item in iterable if condition]


# In[107]:


numbers = [1,2,3,4,5,6,7]
square = []
for i in numbers:
    square.append(i**2)


# In[108]:


square


# In[109]:


square = [i**2 for i in numbers]
square


# In[110]:


numbers = [1,2,3,4,5,6,7]
square = []
for i in numbers:
    if i % 2 == 0:
        square.append(i**2)
square


# In[111]:


square = [i**2 for i in numbers if i % 2 == 0]
square


# In[112]:


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for row in matrix for num in row]


# In[113]:


[num for row in matrix for num in row if num % 2 == 0]


# In[114]:


{x : x**2 for x in numbers}


# In[115]:


{x**2 for x in numbers}


# In[116]:


numbers


# In[117]:


[(lambda x: x+2)(i) for i in numbers]


# In[118]:


[(lambda x: x+2)(i) for i in numbers if i % 2 == 0]


# ### Importing Libraries

# In[119]:


get_ipython().system('pip install scikit-learn')


# In[ ]:


# tensorflow cheatsheet


# In[120]:


import math


# In[121]:


math.sin(90)


# In[122]:


math.factorial(3)


# In[123]:


import tensorflow as tf


# In[127]:


from math import sin, cos, tan


# In[125]:


cos(90)


# In[126]:


tan(90)


# In[128]:


from math import *


# In[129]:


factorial(4)


# ### Libraries Operations

# #### Math Libraries

# In[130]:


import math


# In[131]:


math.sqrt(16)


# In[132]:


math.pow(2,3)


# In[133]:


math.factorial(4)


# In[135]:


math.sin(90), math.sin(math.pi/2)


# In[137]:


math.asin(1)


# In[139]:


math.ceil(4.7), math.floor(4.7)


# In[144]:


math.log(10, 2), math.log(10, 10)


# In[141]:


math.log2(10)


# In[143]:


math.log10(10)


# In[145]:


math.e, math.pi


# #### Datetime

# In[147]:


import datetime as dt


# In[149]:


str(dt.date.today())


# In[151]:


dt.date(2024,9,10)


# In[152]:


dt.datetime.now().time()


# In[153]:


str(dt.datetime.now().time())


# In[154]:


today = dt.date.today()
print(today)


# In[156]:


print(today - dt.timedelta(days=5))


# In[157]:


today.strftime("%A, %B %d, %Y")


# In[162]:


today.strftime("%a, %b %d, %y")


# #### Random Library

# In[163]:


import random as rd


# In[171]:


rd.randint(1,20)


# In[176]:


rd.random()


# In[179]:


choices = ["apple", "mango", "pineapple"]
rd.choice(choices)


# In[183]:


rd.choices(choices, k=2)


# In[186]:


rd.shuffle(choices)


# In[187]:


choices


# In[195]:


rd.seed(13)
rd.randint(1,10)


# ### Error handling

# In[196]:


print("hello world"


# In[197]:


1/0


# In[198]:


print(x=4)


# In[200]:


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("oops! That's not a valid number")


# In[203]:


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("oops! That's not a valid number")


# In[204]:


try:
    result = 10/2
except:
    print("There is an error!!!")
else:
    print(result)


# In[205]:


try:
    result = 10/0
except:
    print("There is an error!!!")
else:
    print(result)


# In[211]:


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
    print(10/num)
except ValueError:
    print("oops! That's not a valid number")
except ZeroDivisionError:
    print("Number cannot be zero")


# In[215]:


try:
    num = int(input("Enter a number: "))
    result = 10/num
except (ValueError, ZeroDivisionError):
    print("There is an error!!!")
else:
    print(result)


# In[230]:


def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return True

try:
    check_age(13)
except ValueError as e:
    print("Error:", e)


# In[231]:


try:
    check_age(13)
except Exception as e:
    print("Error:", e)


# In[232]:


try:
    result = 10 / 0 
except Exception as e:
    print("Error:", e)


# In[237]:


try:
    result = 10 / 0 
    print(result)
except Exception as e:
    print("Error:", e)
finally:
    print("hey")


# In[238]:


try:
    result = 10 / 0
    print(result)
except Exception as e:
    print("Error:", e)
else:
    print("hey")


# In[ ]:


FileNotFoundError, PermissionError, Exception


# ### Guess Game

# In[239]:


import random as rd
import time


# In[241]:


print("Think of any number between 0-100 and keep it with you, let me find out!!")
time.sleep(5)

min_val = 0 
max_val = 100

attempt = 0

while True:
    computer = rd.randint(min_val, max_val)
    print ("\nIsn't it %d ?"%computer)
    attempt += 1

    user = input("Enter the option \n a.high \n b.low \n c.Bingo \n")
    
    if user == "high" or user == "a":
        max_val = computer - 1
    
    elif user == "low" or user == "b":
        min_val = computer + 1
    
    elif user == "bingo" or user == "c":
        print ("\nThe number is in your mind is %d and computer took %d attempts"%(computer,attempt))
        break
    else:
        print ("\nPlease enter the valid option")


# ### FIle Operations

# #### txt file operations

# In[305]:


filePath = "./output.txt"


# In[306]:


file = open(filePath, "r")


# In[307]:


content = file.read()


# In[309]:


print(content)


# In[296]:


file.close()


# In[297]:


with open(filePath, "r") as file:
    content = file.read()
    content


# In[304]:


filePath = "./output.txt"
with open(filePath, "w") as file:
    file.write("this is a sample content for the txt file\n")
    file.write("Another line of text")


# In[311]:


with open(filePath, "r") as file:
    for line in file:
        print(line.strip())
        input()


# #### CSV files

# In[312]:


import csv


# In[313]:


csvFilePath = "./csvFile.csv"


# In[314]:


data = [
    ['Name', 'Age', 'City'],
    ['John', 28, 'New York'],
    ['Jane', 32, 'Los Angeles'],
    ['Mike', 25, 'Chicago']
]


# In[315]:


with open(csvFilePath, "w", newline='') as file:
    csvWriter = csv.writer(file)
    csvWriter.writerows(data)


# In[334]:


with open(csvFilePath, "r") as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        print(row)


# In[333]:


with open(csvFilePath, "r") as file:
    csvReader = csv.DictReader(file)
    for row in csvReader:
        print(row)


# In[331]:


dictData = [
    {'Name': 'John', 'Age': '30', 'City': 'New York'},
    {'Name': 'Jane', 'Age': '35', 'City': 'Los Angeles'},
    {'Name': 'Mike', 'Age': '40', 'City': 'Chicago'}
]


# In[332]:


with open(csvFilePath, "w", newline='') as file:
    fieldNames = ['Name', 'Age', 'City']
    csvWriter = csv.DictWriter(file, fieldnames=fieldNames)
    csvWriter.writeheader()
    csvWriter.writerows(dictData)


# #### Json File

# In[337]:


import json


# In[335]:


jsonPath = "./jsonFIle.json"


# In[336]:


data = {'Name': 'John', 'Age': '30', 'City': 'New York'}


# In[338]:


with open(jsonPath, "w") as file:
    json.dump(data, file, indent=4)


# In[340]:


with open(jsonPath, "r") as file:
    data = json.load(file)
    print(data)


# ### Pandas Library

# In[ ]:


get_ipython().system('pip install pandas')


# In[344]:


import pandas as pd


# In[345]:


data = [10,20,30,40,50]


# In[346]:


pd.Series(data)


# In[347]:


pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])


# In[348]:


dict_data = {'apples': 10, 'bananas': 20, 'cherries': 30}


# In[349]:


pd.Series(dict_data)


# In[350]:


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}


# In[351]:


df = pd.DataFrame(data)


# In[352]:


df


# In[353]:


data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[354]:


df = pd.DataFrame(data, columns=["A", "B", "C"], index=[1,2,3])


# In[355]:


df


# In[367]:


csvData = pd.read_csv("./csvFile.csv")


# In[368]:


csvData


# In[369]:


csvData["Salary"] = [5000, 8500, 6500]


# In[370]:


csvData


# In[372]:


csvData.drop("City", axis=1)


# In[373]:


csvData = pd.read_csv("./data.csv")


# In[374]:


csvData.head(3)


# In[375]:


csvData.tail(3)


# In[376]:


csvData.shape


# In[365]:


csvData.describe()


# In[366]:


csvData


# In[378]:


csvData.groupby("category").sum()


# In[379]:


csvData.groupby("category")['feature1'].transform('sum')


# In[380]:


csvData.sort_values("category")


# In[382]:


csvData.isna().any()


# In[383]:


csvData.drop_duplicates(subset="feature1")


# ### Example : hangman game

# In[279]:


f = open("wordList.txt", "r")
lines = f.readlines()
words = [i.strip() for i in lines]


# In[280]:


words 


# In[281]:


import random as rd


# In[282]:


picked = rd.choice(words)


# In[283]:


picked


# In[290]:


originalWordList = list(picked)
answerList = list("_" * len(picked))
print("The word has",len(picked),"letters:", answerList)
print(f"The starting letter of the word is {originalWordList[0]}")


# In[291]:


attempt = len(picked) + 2
while True:
    guessChar = input("Enter your guess: ").upper()
    attempt -= 1
    
    if guessChar in originalWordList:
        indices = [i for i,x in enumerate(originalWordList) if x == guessChar]
        for index in indices:
            answerList[index] = guessChar
        print("Current Progress:", answerList)
    else:
        print("Wrong guess!!!")
    
    if "_" not in answerList:
        print("Congratulations! you have guessed the word", picked)
        print("You won in",attempt,"attempts.")
        break
    
    if attempt <= 0:
        print("No attempts Try")


# In[ ]:


f = open("wordList.txt", "r")
lines = f.readlines()
words = [i.strip() for i in lines]
picked = rd.choice(words)

originalWordList = list(picked)
answerList = list("_" * len(picked))
print("The word has",len(picked),"letters:", answerList)
print(f"The starting letter of the word is {originalWordList[0]}")

attempt = len(picked) + 2
while True:
    guessChar = input("Enter your guess: ").upper()
    attempt -= 1
    
    if guessChar in originalWordList:
        indices = [i for i,x in enumerate(originalWordList) if x == guessChar]
        for index in indices:
            answerList[index] = guessChar
        print("Current Progress:", answerList)
    else:
        print("Wrong guess!!!")
    
    if "_" not in answerList:
        print("Congratulations! you have guessed the word", picked)
        print("You won in",attempt,"attempts.")
        break
    
    if attempt <= 0:
        print("No attempts Try")


# ### Project: GooglePay Expense Sharing

# **Business Use Case**: Friends want to easily track shared expenses and settle debts using a simple tool similar to Google Pay.
# 
# 
# **Description**: Create a Python program that helps friends manage shared expenses and calculate who owes whom. Suppose there are three friends—Alice, Bob, and Carol. They went on a trip and shared expenses for accommodation and meals. The program will allow them to input these expenses, calculate how much each person needs to pay or be reimbursed, and display the final settlement amounts.
# 

# In[ ]:


get_ipython().system('pip install numpy prettytable')


# In[254]:


import numpy as np
from prettytable import PrettyTable


# In[269]:


friends = ["Alice", "Bob", "Carol", "David"]
expense_matrix = np.zeros((len(friends), len(friends)))  # Rows: Who paid, Columns: Who it's for


# In[270]:


expense_matrix


# In[271]:


def add_expense(payer, beneficiaries, amount):
    payer_idx = friends.index(payer)
    share_per_person = amount / len(beneficiaries)
    for beneficiary in beneficiaries:
        beneficiary_idx = friends.index(beneficiary)
        expense_matrix[payer_idx][beneficiary_idx] += share_per_person


# In[272]:


def calculate_settlements():
    total_paid = np.sum(expense_matrix, axis=1)  # How much each person paid
    total_owed = np.sum(expense_matrix, axis=0)  # How much each person owes
    net_balance = total_paid - total_owed  # Positive: person should receive, Negative: person owes
    return net_balance


# In[273]:


def display_settlements():
    settlements = calculate_settlements()

    table = PrettyTable()
    table.field_names = ["Friend", "Settlement"]

    for i, friend in enumerate(friends):
        if settlements[i] > 0:
            table.add_row([friend, f"Should Receive ₹{settlements[i]:.2f}"])
        elif settlements[i] < 0:
            table.add_row([friend, f"Owes ₹{-settlements[i]:.2f}"])
        else:
            table.add_row([friend, "Is Settled"])

    print("\nFinal Settlements:")
    print(table)


# In[274]:


def suggest_payments():
    settlements = calculate_settlements()

    creditors = [(friends[i], amt) for i, amt in enumerate(settlements) if amt > 0]
    debtors = [(friends[i], -amt) for i, amt in enumerate(settlements) if amt < 0]

    transactions = []

    # Match debtors to creditors
    while debtors and creditors:
        debtor, debt_amount = debtors.pop(0)
        creditor, credit_amount = creditors.pop(0)

        payment = min(debt_amount, credit_amount)
        transactions.append((debtor, creditor, payment))

        # Adjust balances
        debt_amount -= payment
        credit_amount -= payment

        # Re-add to list if any balance remains
        if debt_amount > 0:
            debtors.insert(0, (debtor, debt_amount))
        if credit_amount > 0:
            creditors.insert(0, (creditor, credit_amount))
    print("\nSuggested Transactions:")
    if transactions:
        for debtor, creditor, amount in transactions:
            print(f"{debtor} should pay ₹{amount:.2f} to {creditor}")
    else:
        print("No transactions needed. Everyone is settled.")


# In[275]:


# Input expenses
add_expense("Alice", ["Alice", "Bob", "Carol"], 1200)   # Alice paid ₹1250 for Alice, Bob, and Carol
add_expense("Bob", ["Bob", "Carol"], 800)               # Bob paid ₹800 for Bob and Carol
add_expense("Carol", ["Alice", "Bob", "Carol", "David"], 1600)  # Carol paid ₹1785 for everyone


# In[276]:


# Display final settlement
display_settlements()


# In[277]:


# Suggest payments to settle debts
suggest_payments()


# ### Linear Regression

# ![formula](https://miro.medium.com/v2/resize:fit:960/0*rHOClzLZwTKY6Q6O.png)

# ![Linear Regression](https://i.ytimg.com/vi/zPG4NjIkCjc/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFIgZShfMA8=&rs=AOn4CLBZnskaRI7tBftWcYmNtmIZv2i-fw)

# ![MSE](https://media.licdn.com/dms/image/v2/D4D12AQElnzGmdRcbWw/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1671516160761?e=1731542400&v=beta&t=wSYDTuPMIcGSFnvj6vhtrACqVS_8uqaFEge05bYR2jg)

# In[ ]:


y = [4, 4]
ypred = [6,2]
error = [-2, 2] = [4, 4] = 4


# ![R-Squared](https://miro.medium.com/v2/resize:fit:1200/1*_mVvAFVEGinHlijmmeWwzg.png)

# In[437]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[433]:


# load dataset
dataset = pd.read_csv("./Advertising.csv", index_col=0)


# In[434]:


dataset.head()


# In[438]:


dataset.shape


# In[436]:


features = dataset.loc[:, "TV":"newspaper"]
output = dataset['sales']


# In[439]:


# spliting dataset
x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.1, random_state=3)


# In[440]:


x_train.shape, x_test.shape


# In[441]:


# define a model
model = LinearRegression()


# In[442]:


# training
model.fit(x_train, y_train)


# In[443]:


ypred = model.predict(x_test)


# In[444]:


ypred


# In[445]:


y_test


# In[446]:


model.coef_


# In[447]:


model.intercept_


# In[448]:


# metrics
mean_squared_error(y_test, ypred)


# In[449]:


r2_score(y_test, ypred)


# In[450]:


# objective-1 how much would i get if i invest 100 in all
model.predict([[100,100,100]])


# In[453]:


# objective-2 in which platform i should invest more
model.predict([[100,150,50]])


# In[454]:


model.predict([[150,150,0]])


# ### Ridge Regression

# ![Ridge Regression](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/2GzY9lVDj2Jdf8de7Kgc9Q.png)

# In[456]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score


# In[485]:


# define a model
model = Ridge(alpha=100)


# In[486]:


# training
model.fit(x_train, y_train)


# In[487]:


ypred = model.predict(x_test)


# In[488]:


ypred


# In[472]:


y_test


# In[489]:


model.coef_


# In[490]:


model.intercept_


# In[491]:


# metrics
mean_squared_error(y_test, ypred)


# In[492]:


r2_score(y_test, ypred)


# ### Logistic Regression

# ![logistic](https://d1.awsstatic.com/sigmoid.bfc853980146c5868a496eafea4fb79907675f44.png)

# ![curve](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/1200px-Logistic-curve.svg.png)

# ![log loss](https://editor.analyticsvidhya.com/uploads/90149Capture0.PNG)

# In[493]:


import numpy as np
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import  LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report, confusion_matrix


# In[494]:


dataset = load_breast_cancer()


# In[495]:


dataset.feature_names


# In[496]:


dataset.target_names


# In[498]:


features = dataset.data
labels = dataset.target


# In[499]:


x_train, x_test, y_train, y_test = train_test_split(features,labels, test_size=0.2, random_state=3)


# In[501]:


x_train.shape, x_test.shape


# In[504]:


model = LogisticRegression(max_iter=500)


# In[505]:


model.fit(x_train, y_train)


# In[506]:


ypred = model.predict(x_test)


# In[508]:


print(classification_report(y_test, ypred))


# In[509]:


print(confusion_matrix(y_test, ypred))


# ### SVM

# ![svm](https://vitalflux.com/wp-content/uploads/2022/08/support-vector-machine-1.png)

# w.x + b = 0
# 
# y(w.x + b) >= 1

# In[512]:


import numpy as np
from sklearn.model_selection import  train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report, confusion_matrix


# In[529]:


model = SVC(kernel="linear", C=1)


# In[530]:


model.fit(x_train, y_train)


# In[531]:


ypred = model.predict(x_test)


# In[532]:


print(classification_report(y_test, ypred))


# In[533]:


print(confusion_matrix(y_test, ypred))


# ### Decision Tree

# Gini Impurity

# ![gini](https://miro.medium.com/v2/resize:fit:928/1*OdxwLHiDtWB9g1RsaTd8Iw.png)

# Information Gain

# ![entropy](https://miro.medium.com/v2/resize:fit:736/1*aRIPv55GHPy7g9OllMvbwg.png)

# ![dataset](https://cdn-images-1.medium.com/v2/resize:fit:1600/1*L3wbmF9htj1PFSCrm-Nr1Q.jpeg)

# In[536]:


entropy_play = - ((9/14 * log2(9/14)) + (5/14 * log2(5/14)))


# In[553]:


entropy_play


# In[ ]:


Test_scenario = "Sunny, Mild, high, True"


# In[537]:


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier


# In[538]:


dataset = pd.read_csv("../PlayTennis.csv")


# In[539]:


dataset.head()


# In[541]:


X = dataset[['Outlook', 'Temperature', 'Humidity', 'Wind']]
y = dataset['Play Tennis']


# In[544]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


# In[545]:


for column in X.columns:
    X[column] = le.fit_transform(X[column])


# In[546]:


X


# In[547]:


model = DecisionTreeClassifier(criterion="entropy")


# In[548]:


model.fit(X, y)


# In[549]:


model.predict([[2,2,0,0]])


# In[550]:


model.predict_proba([[2,2,0,0]])


# In[551]:


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# In[552]:


plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)


# ### Ensemble Method - Random Forest

# ![ensemble](https://cdn.corporatefinanceinstitute.com/assets/ensemble-methods.png)

# ![rf](https://miro.medium.com/v2/resize:fit:1010/1*R3oJiyaQwyLUyLZL-scDpw.png)

# In[555]:


import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


# In[563]:


url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)


# In[564]:


titanic_data.head()


# In[566]:


titanic_data.isna().any()


# In[565]:


titanic_data.isnull().any()


# In[567]:


titanic_data.shape


# In[568]:


titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)
titanic_data['Cabin'].fillna(titanic_data['Cabin'].mode()[0], inplace=True)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)


# In[569]:


titanic_data.head()


# In[570]:


titanic_data.isna().any()


# In[571]:


titanic_data['Embarked'] = titanic_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
titanic_data['Sex']= titanic_data['Sex'].map({'male':0, "female":1})


# In[572]:


titanic_data.head()


# In[573]:


X = titanic_data[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = titanic_data['Survived']


# In[574]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


# In[579]:


model = RandomForestClassifier(n_estimators=500)


# In[580]:


model.fit(X_train,y_train)


# In[581]:


ypred = model.predict(X_test)


# In[582]:


print(classification_report(y_test, ypred))


# ### Gradient Boosting

# ![gradient](https://media.geeksforgeeks.org/wp-content/uploads/20200721214745/gradientboosting.PNG)

# In[1]:


import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


# In[2]:


url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)


# In[3]:


titanic_data.head()


# In[4]:


titanic_data.isna().any()


# In[ ]:


titanic_data.isnull().any()


# In[5]:


titanic_data.shape


# In[6]:


titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)
titanic_data['Cabin'].fillna(titanic_data['Cabin'].mode()[0], inplace=True)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)


# In[7]:


titanic_data.head()


# In[8]:


titanic_data.isna().any()


# In[9]:


titanic_data['Embarked'] = titanic_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
titanic_data['Sex']= titanic_data['Sex'].map({'male':0, "female":1})


# In[10]:


titanic_data.head()


# In[11]:


X = titanic_data[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = titanic_data['Survived']


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


# In[33]:


model = GradientBoostingClassifier(n_estimators=500, learning_rate=0.1, max_depth=3)


# In[34]:


model.fit(X_train, y_train)


# In[35]:


ypred = model.predict(X_test)


# In[36]:


print(classification_report(y_test, ypred))


# ### K-Means Clustering 

# ![K-means](https://images.squarespace-cdn.com/content/v1/5acbdd3a25bf024c12f4c8b4/1608407348392-22767PJ7RQ85BD5RLSLZ/k-means-clustering.png
# )

# ![euclidean](https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL2Rpc3RhbmNlLWZvcm11bGEuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjoiMTIwMCJ9fX0=)

# In[37]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# In[38]:


X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=3)


# In[42]:


plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Sample Data Points')
plt.show()


# In[43]:


kmeans = KMeans(n_clusters=4)


# In[44]:


kmeans.fit(X)


# In[45]:


y_kmeans = kmeans.predict(X)


# In[46]:


y_kmeans


# In[47]:


plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')


# ### Hierarchical Clustering

# ![dendrogram](https://miro.medium.com/v2/resize:fit:979/0*R8acBZk1JrLw4Hg1.png)

# In[49]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering


# In[50]:


X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)
plt.scatter(X[:, 0], X[:, 1])
plt.show()


# In[51]:


Z = linkage(X, method='ward') # Ward method minimizes variance within clusters
dendrogram(Z)
plt.show()


# In[53]:


agg_cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
y_pred = agg_cluster.fit_predict(X)

# Plot the clustered data
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()


# ### DBSCAN

# ![dbscan](https://miro.medium.com/v2/resize:fit:1400/0*SOUGjZwam-QJdp0Q)

# ![points](https://miro.medium.com/v2/resize:fit:627/1*yT96veo7Zb5QeswV7Vr7YQ.png)

# In[54]:


from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generating sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Visualizing the data
plt.scatter(X[:, 0], X[:, 1])
plt.show()


# In[59]:


# Applying DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X)

# Plotting the clustered data
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='plasma')
plt.show()


# ### Gaussian Mixture Models (GMM) Clustering

# ![gaussian](https://miro.medium.com/v2/resize:fit:753/1*EJsRv-8nUeqYOOVxBhol5A.png)

# ![formula](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/09/image-1.png)

# In[66]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

# Create synthetic data
X, y = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=2)

# Plot the raw data
plt.scatter(X[:, 0], X[:, 1], c='gray', marker='o', s=40)
plt.title("Raw Data")
plt.show()


# In[67]:


# Fit a GMM model
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

# Predict the cluster labels
labels = gmm.predict(X)

# Plot the clustered data
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.title("Clustered Data using GMM")
plt.show()


# In[68]:


# Get the probability of each point belonging to each cluster
probs = gmm.predict_proba(X)

# Plot the probability of each point belonging to a specific cluster
plt.scatter(X[:, 0], X[:, 1], c=probs[:, 1], cmap='coolwarm', s=40)
plt.title("Soft Clustering Probabilities")
plt.show()


# ### PCA

# ![PCA](https://dimensionless.in/wp-content/uploads/2019/07/pca2.png)

# ![formula](https://emergingindiagroup.com/wp-content/uploads/2024/05/article1.png)

# In[1]:


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


# In[70]:


data = load_iris()
X = data.data
y = data.target


# In[74]:


from sklearn.preprocessing import StandardScaler
X_standardized = StandardScaler().fit_transform(X)


# In[76]:


X[:5]


# In[77]:


X_standardized[:5]


# In[78]:


pca = PCA(n_components=2)


# In[79]:


X_pca = pca.fit_transform(X_standardized)


# In[80]:


X_pca[:5]


# In[81]:


# Plotting the PCA result
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA on Iris Dataset')
plt.colorbar()
plt.show()


# ### Cross-Validation and Hyperparameter Tuning

# ![crossValidation](https://miro.medium.com/v2/resize:fit:940/1*lOZqYqwmuW1lg6fitwqXxA.png)

# In[2]:


import numpy as np
from sklearn.model_selection import  train_test_split, KFold
from sklearn.linear_model import  LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# In[84]:


dataset = load_breast_cancer()


# In[85]:


dataset.feature_names


# In[86]:


dataset.target_names


# In[87]:


features = dataset.data
labels = dataset.target


# In[88]:


model = LogisticRegression()


# In[89]:


scores = []
kf = KFold(n_splits=5,shuffle=True, random_state=42)


# In[92]:


for train_index, test_index in kf.split(features):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = labels[train_index], labels[test_index]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    scores.append(accuracy)


# In[94]:


np.mean(scores)


# ![hyperparameter](https://researchgate.net/profile/Hana-Alkassar/publication/360189662/figure/fig1/AS:1149088523390989@1650975461937/Hyperparameter-tuning-using-five-fold-cross-validation-GridSearchCV.png)

# In[ ]:


from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Define the parameter grid
param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

X = features
y = labels

# Random Forest model
rf = RandomForestClassifier(random_state=42)

# Grid Search with Cross-Validation
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)

# Fit model
grid_search.fit(X, y)

# Best parameters
print(f'Best parameters: {grid_search.best_params_}')
print(f'Best cross-validation score: {grid_search.best_score_}')


# In[4]:


url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)


# In[5]:


titanic_data.head()


# In[ ]:


titanic_data.isna().any()


# In[ ]:


titanic_data.isnull().any()


# In[ ]:


titanic_data.shape


# In[6]:


titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)
titanic_data['Cabin'].fillna(titanic_data['Cabin'].mode()[0], inplace=True)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)


# In[7]:


titanic_data.head()


# In[8]:


titanic_data.isna().any()


# In[9]:


titanic_data['Embarked'] = titanic_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
titanic_data['Sex']= titanic_data['Sex'].map({'male':0, "female":1})


# In[10]:


titanic_data.head()


# In[11]:


X = titanic_data[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = titanic_data['Survived']


# In[107]:


X, Y


# In[12]:


# Define the parameter grid
param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Random Forest model
rf = RandomForestClassifier(random_state=42)

# Grid Search with Cross-Validation
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)

# Fit model
grid_search.fit(X, y)

# Best parameters
print(f'Best parameters: {grid_search.best_params_}')
print(f'Best cross-validation score: {grid_search.best_score_}')


# In[ ]:


from sklearn.model_selection import RandomizedSearchCV


# ### Stacking Model

# ![stacking](https://miro.medium.com/v2/resize:fit:1400/1*0qQTUDfImZYQBsyn9F6dpw.png)

# ![stacking](https://media.geeksforgeeks.org/wp-content/uploads/20190515104518/stacking.png)

# In[13]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.metrics import accuracy_score


# In[14]:


X.head()


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


# In[20]:


# Define base models
base_models = [
    ('rf', RandomForestClassifier(n_estimators=500, random_state=42)),
    ('gb', GradientBoostingClassifier(n_estimators=500, random_state=42)),
    ('knn', KNeighborsClassifier())
]


# In[21]:


# Define meta-model
meta_model = LogisticRegression()


# In[22]:


stacking_clf = StackingClassifier(estimators=base_models, final_estimator=meta_model, cv=5)


# In[23]:


# Train the stacking model
stacking_clf.fit(X_train, y_train)

# Predictions
y_pred = stacking_clf.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Stacking Model Accuracy: {accuracy * 100:.2f}%")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




