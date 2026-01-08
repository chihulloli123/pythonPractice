#print("hello, world")

#if 5 >2:
 #   print("tahlapi is greater than tuklo!")

#x = 5
#y = "Hello, World!"
#didnt run because there was no print statement

#print("Amanda")
#print("Cari")
#print("Perez")

#print("Hello"); print("How are you"); print(("Bye bye!"))

#print('hello, world')

#print("Hello, world", end=" ")
#print("I will print on the same line.")

#print(3+2)
#print(2*5)

#print("I am", 35, "years old.")

#x = 5
#y = "Johnson"
#print(type(x))
#print(type(y))

#x,y,z = "Orange", "Banana", "Cherry"
#print(x)
#print(y)
#print(z)

#x = y = z = "Orange"
#print(x)
#print(y)
#print(z)

#if you have a colletion of values in a list, tuple, etc. Python allows 
#you to extract the values into variables. This is called unpacking. 
#fruits = ["aPple", "bananA", "cHerry"]
#x,y,z = fruits
#print(x)
#print(y)
#print(z)

#x = "Johnson"
#y = "Perez"
#z = "Icebox"
#print(x + y + z)

#x = 5
#y = 10
#print(x + y)

#x = "awesome"

#def myfunc():
 #   x = "fantastic"
 #  print("Python is " + x)

#myfunc()

#print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used
#inside that function. To create a global use the keyword
#def myfunc():
 #   global x
  #  x = "fantastic"

#myfunc()

#print("Print is " + x)

#x = 1
#y = 2.8
#z = 1j

#print(type(x))
#print(type(y))
#print(type(z))
 
 #x = 1
 #y = 2.8
 #z = 1j

 #a = float(x)
 #b = int(y)
 #c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))
#import random

#print(random.randrange(1,10))

#print("It's alright")
#print("He is called 'Johnny'")
#print('He is called "Johnny"')

#a = "Hello"
#print(a)

#a = "Hello World!"
#print(a[4])

#for x in "banana":
 # print(x)

#a = "Hello, World!"
#print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in
#txt = "The best things in life are free!"
#print("free" in txt)

#txt = "The best things in life are free!"
#if "expensive" not in txt:
#  print("no, 'expensive' is NOT present.")

#b = "Hello, World!"
#print(b[3:])

#a = "Hello, World!"
#print(a.split(","))

#age = 43
#txt = f"My name is John, I am {age}"
#print(txt)

#price = 59
#txt = f"The price is {price} dollars"
#print(txt)

#price = 59
#txt = f"The price is {price:.2f} dollars"
#print(txt)

#txt = f"The price is {20 * 59} dollars"
#print(txt)

#print(10>9)
#print(10 == 9)
#print(10 < 9)

#a = 200
#b = 33

#if b > a:
 # print("b is greater than a")
#else:
 #   print("b is not greater than a")

#print(bool("Hello"))
#print(bool(15))

#x = "Hello"
#y = 15

#print(bool(x))
#print(bool(y))

#print(bool("abc"))
#print(bool(123))
#print(bool(["apple", "cherry", "banana"]))

#print(bool(False))
#print(bool(None))
#print(bool(0))
#print(bool(""))
#print(bool(()))
#print(bool([]))
#print(bool({}))

#class myclass():
#  def __len__(self):
#    return 0

#myobj = myclass()
#print(bool(myobj))

#def myFunction() :
#   return True

#print(myFunction())

#def myFunction() :
#  return True

#if myFunction():
#  print("YES!")
#else:
#  print("NO!")

#x = 200
#print(isinstance(x, int))

#x = 15
#y = 4

#print(x+y)
#print(x-y)
#print(x*y)
#print(x/y)
#print(x%y)
#print(x**y)
#print(x//y)

#x=12
#y=5

#print(x/y)

#x=12
#y=5

#print(x//y)

#numbers = [1, 2, 3, 4, 5]
#count = len(numbers)
#if count > 3:
#  print(f"List has {count} elements")
#if (count := len(numbers)) > 3:
#  print(f"List has {count} elements")

#x = ["apple", "banana"]
#y = ["apple", "banana"]
#z = x

#print(x is z)
#print(x is y)
#print(x == y)

#x = ["apple", "banana"]
#y = ["apple", "banana"]

#print(x is not y)

#x = [1, 2, 3]
#y = [1, 2, 3]

#print(x == y)
#print(x is y)

#print(6 & 3)
#print(6 | 3)
#print(6 ^ 3)

#thislist = ["apple", "banana", "cherry", "apple", "cherry"]
#print(thislist)
#print(len(thislist))

#thislist = ["apple", "banana", "cherry"]
#print(thislist[1])

#thislist = ["apple", "banana", "cherry"]
#print(thislist[-1])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:5])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[:4])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[-4:-1])

#thislist = ["apple", "banana", "cherry"]
#if "apple" in thislist:
#  print("Yes, 'apple' is in the fruits list")

#thislist = ["apple", "banana", "cherry"]
#thislist[1] = "blackcurrant"
#print(thislist)

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist[1:3] = ["blackcurrant", "watermelon"]
#print(thislist)


#thislist = ["apple", "banana", "cherry"]
#thislist[1:2] = ["blackcurrent", "watermelon"]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist[1:3] = ["watermelon"]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.insert(2, "watermelon")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.append("orange")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.insert(1, "orange")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#tropical = ["mango", "pineapple", "papaya"]
#thislist.extend(tropical)
#print(thislist)

