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


#thislist = ["apple", "banana", "cherry"]
#thistuple = ("kiwi", "orange")
#thislist.extend(thistuple)
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.remove("banana")
#print(thislist)

#messages = ["classified", "routine", "classified", "urgent"]
#messages.remove("classified")
#print(messages)

# Simulated incoming intelligence message queue
#message_queue = [
#    "routine: system check",
#    "classified: troop movement",
#    "classified: nuclear site activity",
#    "urgent: UAV down",
#    "routine: supply drop successful",
#    "classified: intercepted transmission"
#]

# Analyst confirms first 'classified' message already processed
#print("Original Queue:")
#print(message_queue)

# Remove the first classified message (already handled)
#for message in message_queue:
#    if "classified" in message:
#        message_queue.remove(message)
#        break  # Only remove the first match

#print("\nUpdated Queue (after removing first processed classified message):")
#print(message_queue)

# Count how many classified messages still remain
#classified_count = sum(1 for msg in message_queue if "classified" in msg)
#print(f"\nClassified messages still pending: {classified_count}")

# Simulate promoting the urgent message to the top of the queue
#urgent_msg = None
#for msg in message_queue:
#    if "urgent" in msg:
#        urgent_msg = msg
#        message_queue.remove(msg)
#        break
#if urgent_msg:
#    message_queue.insert(0, urgent_msg)

#print("\nQueue after promoting urgent message:")
#print(message_queue)
#intel_queue = [
#    "classified: troop movement",
#    "routine: supply report",
#    "urgent: cyber breach",
#    "classified: missile test",
#    "routine: weather update",
#    "classified: border drone footage"
#]

# Step 1: Remove the first 'classified' message (processed by analyst)
#for msg in intel_queue:
#    if "classified" in msg:
#        intel_queue.remove(msg)
#        break

# Step 2: Promote all 'urgent' messages to the front
#urgent_messages = [msg for msg in intel_queue if "urgent" in msg]
#for msg in urgent_messages:
#    intel_queue.remove(msg)
#intel_queue = urgent_messages + intel_queue

# Step 3: Add new incoming message
#intel_queue.append("classified: intercepted communication")

# Step 4: Count messages by category
#classified_count = sum("classified" in msg for msg in intel_queue)
#urgent_count = sum("urgent" in msg for msg in intel_queue)
#routine_count = sum("routine" in msg for msg in intel_queue)

# Display mission-ready intel queue
#print("\n📡 Current Intel Queue:")
#for i, msg in enumerate(intel_queue, 1):
#    print(f"{i}. {msg}")

# Display categorized counts
#print(f"\n Classified: {classified_count}")
#print(f" Urgent: {urgent_count}")
#print(f" Routine: {routine_count}")

#thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
#thislist.remove("banana")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.pop()
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#del thislist[0]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#del thislist

#thislist = ["apple", "banana", "cherry"]
#thislist.clear()
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#for x in thislist:
#  print(x)

#thislist = ["apple", "banana", "cherry"]
#for i in range(len(thislist)):
#  print(thislist[i])

#intel_feed = [
#"SIGINT: comms intercept", 
#"HUMINT: troop movement", 
#"IMINIT: satellite scan"
#]
#packet_index = 0

#while packet_index < len(intel_feed):
#  print(intel_feed[packet_index])
#  packet_index += 1

#  def log_event(packet):
#    print(f"Processing packet: {packet}")

#intel_feed = ["SIGINT: comms intercept", "HUMINT: troop movement", "IMINT: satellite scan"]
#packet_index = 0

#while packet_index < len(intel_feed):
#    log_event(intel_feed[packet_index])
#    packet_index += 1

#thislist = ["apple", "banana", "cherry"]
#i = 0
#while i < len(thislist):
#  print(thislist[i])
#  i = i + 1

#thislist = ["apple", "banana", "cherry"]
#[print(x) for x in thislist]

#intel_stream = [
#  "HUMINT: base chatter",
#  "SIGINT: encrypted message",
#  "IMINT: drone scan",
#  "OSINT: forum post",
#  "HUMINT: captured audio",
#  "SOCINT: behavior pattern"
#]

#flagged_signals = []
#filter for any signals containing the term "HUMINT" (Human Intelligence)
#for signal in intel_stream:
#  if "HUMINT" in signal:
#    flagged_signals.append(signal)

#print("Flagged Signals for Review:")
#print(flagged_signals)

#ntel_stream = [
 #   "HUMINT: base chatter",
 #   "SIGINT: encrypted message",
 #   "IMINT: drone scan",
 #   "OSINT: forum post",
 #   "HUMINT: captured audio",
 #   "SOCINT: behavior pattern"
#]

# Pull only signals involving HUMINT
#humint_signals = [signal for signal in intel_stream if "HUMINT" in signal]

#print("HUMINT Signals for Analyst Review:")
#print(humint_signals)

#intel_sources = ["SIGINT", "HUMINT", "IMINT", "OSINT", "MASINT"]
#intel_sources.sort()
#print(intel_sources)

#threat_levels = [3, 5, 1, 4, 2]
#threat_levels.sort()
#print(threat_levels)

#target_priority = [82, 99, 30, 45, 71]
#target_priority.sort(reverse=True)
#print(target_priority)

#def myfunc(n):
#  return abs(n-50)

#thislist = [100, 50, 65, 82, 23]
#thislist.sort(key=myfunc)
#print(thislist)

#thislist = ["banana", "Orange", "Kiwi", "cherry"]
#thislist.sort()
#print(thislist)

#thislist = ["banana", "Orange", "Kiwi", "cherry"]
#thislist.sort(key = str.lower)
#print(thislist)

#thislist = ["banana", "Orange", "Kiwi", "cherry"]
#thislist.reverse()
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#mylist = thislist.copy()
#print(mylist)

#thislist = ["apple", "banana", "cherry"]
#mylist = list(thislist)
#print(mylist)

#thislist = ["apple", "banana", "cherry"]
#mylist = thislist[:]
#print(mylist)

#list1 = ["a", "b", "c"]
#list2 = [1, 2, 3]

#list3 = list1 + list2
#print(list3)

#list1 = ["a", "b", "c"]
#list2 = [1, 2, 3]

#for x in list2:
#  list1.append(x)

#print(list1)

#list1 = ["a", "b", "c"]
#list2 = [1, 2, 3]

#list1.extend(list2)
#print(list1)

#thistuple = ("apple", "banana", "cherry", "apple", "cherry")
#print(thistuple)

#thistuple = ("apple", "banana", "cherry")
#print(len(thistuple))

#to create a tuple with only one item, you have to add a comma after the item, otherwise Python wil
#not recognize it as a tuple..
#thistuple = ("apple",)
#print(len(thistuple))

#tuple1 = ("apple", "banana", "cherry")
#tuple2 = (1, 5, 7, 9, 3)
#tuple3 = (True, False, True)

#print(type(tuple1))
#print(type(tuple2))
#print(type(tuple3))

#records = [
#    (100234, "IT", True),
#    (100235, "HR", False),
#    (100236, "IT", True),
#    (100237, "Finance", True),
#    (100238, "HR", True),
#]

#def count_active_by_department(records):
#    result = {}

#    for emp_id, department, is_active in records:
#        if is_active:
#            if department not in result:
#                result[department] = 0
#            result[department] += 1

#    return result

#output = count_active_by_department(records)
#print(output)

#thistuple=("apple", "banana", "cherry")
#print(thistuple[1])

#thistuple=("apple", "banana", "cherry")
#print(thistuple[-1])

#thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[2:5])

#thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[:4])

#thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[2:])

#thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[-4:-1])

#thistuple=("apple", "banana", "cherry")
#if "apple" in thistuple:
#  print("yes, 'apple' is in the fruits tuple")

#onboarding_steps = ("Account Setup", "Orientation", "Security Briefing")
#steps_list = list(onboarding_steps)

#for i in range(len(steps_list)):
#  if steps_list[i] == "Orientation":
#    steps_list[i] = "Intro"

#onboarding_steps = tuple(steps_list)

#print(onboarding_steps)

# Immutable original data (e.g., coming from Foundry pipeline or upstream model)
#departments = ("Homeland Security", "Department of Defense", "Cyber Command")

# Step 1: Convert tuple to list to make changes
#editable_departments = list(departments)

# Step 2: Apply rename
#for i in range(len(editable_departments)):
#    if editable_departments[i] == "Department of Defense":
#        editable_departments[i] = "Department of War"

# Step 3: Freeze it again to avoid accidental mutation later
#departments = tuple(editable_departments)

# Final result
#print(departments)

#thistuple = ("apple", "banana", "cherry")
#y = list(thistuple)
#y.append("orange")
#thistuple = tuple(y)
#print(thistuple)

#thistuple = ("apple", "banana", "cherry")
#y = list(thistuple)
#y.remove("apple")
#thistuple = tuple(y)
#print(thistuple)

#fruits = ("apple", "banana", "cherry")

#(green, yellow, red) = fruits

#print(green)
#print(yellow)
#print(red)

#def escalate_alerts(alert_id, category_):
#  print(f"Escalating {alert_id}: {category}")
  


#alert = (3862, "2026-01-08T09:15z", "System Breach", "High")

#id, timestamp, category, severity = alert
#if severity == "High":
#  escalate_alerts(id, category)

#fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

#(green, yellow, *red) = fruits

#print(green)
#print(yellow)
#print(red)

#fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#(green, *tropic, red) = fruits
#print(green)
#print(tropic)
#print(red)

#thistuple = ("apple", "banana", "cherry")
#for x in thistuple: 
#  print(x) 

#a = 33 
#b = 200
#if b > a:
#  print("b is greater than a")

#number = 15
#if number > 0:
#  print("The number is positive")
#age = 20
#if age >= 18:
#  print("You are an adult")
#  print("You can vote")
#  print("You have full legal rights")

#is_logged_in = True
#if is_logged_in:
#  print("Welcome back!")

#a = 33
#b = 33 
#if b > a:
#  print("b is greater than a")
#elif a == b:
#  print("a and b are equal")

#score = 75

#if score >= 90:
#  print("Grade: A")
#elif score >= 80:
#  print("Grade: B")
#elif score >= 70:
#  print("Grade: C")
#elif score >= 60:
#  print("Grade: D")

#age = 25

#if age < 13:
#  print("You are a child")
#elif age < 20:
#  print("You are a teenager")
#elif age < 65:
#  print("You are an adult")
#elif age >= 65:
#  print("you are a senior")

day = 3

#if day == 1:
#  print("Monday")
#elif day == 2:
#  print("Tuesday")
#elif day == 3:
#  print("Wednesday")
#elif day == 4:
#  print("Thursday")
#elif day == 5:
#  print("Friday")
#elif day == 6:
#  print("Saturday")
#elif day == 7:
#  print("Sunday")

#a = 5
#b = 22
#if a > b: print("a is greater than b")
#a = 2
#b = 0

#print("A") if a > b else print("B")

#a = 1
#b = 20
#bigger = a if a > b else b
#print("Bigger is", bigger)

#a = 330
#b = 330
#print("A") if a > b else print("=") if a == b else print("B")

#x = 15
#y = 20 
#max_value = x if x > y else y
#print("Maximum value:", max_value)

#username = ""
#display_name = username if username else "Guest"
#print("Welcome,", display_name)

#a = 200
#b = 33
#c = 500
#if a > b and c > a:
#  print("Both conditions are True")

#a = 200
#b = 33
#c = 500
#if a > b or a > c:
#  print("At least one of the conditions is Ture")

#a = 33
#b = 200
#if not a > b:
#  print("a is NOT greater than b")

#age = 25
#is_student = False
#has_discount_code = True

#if (age < 18 or age > 65) and not is_student or has_discount_code:
#  print("discount applies!")

#temperature = 25
#is_raining = False
#is_weekend = True

#if(temperature > 20 and not is_raining) or is_weekend:
#  print("Great day for outdoor activities!")
#username = "Tobias"
#password = "secret123"
#is_verified = True

#if username and password and is_verified:
#  print("login successful")
#else:
#  print("login failed")

#score = 85

#if score >= 0 and score <= 100:
#  print("Valid score")
#else:
#  print("Invalid score")

#x = 111

#if x > 10:
#  print("Above ten,")
#  if x > 20:
#    print("and also above 20!")
#  else:
#    print("but not above 20.")

#age = 25
#has_license = True

#if age >= 18:
#  if has_license:
#    print("You can drive")
#  else:
#    print("You need a license")
#else:
#    print("You are too young to drive")

#temperature = 25
#is_sunny = True

#if temperature > 20:
#  if is_sunny:
#    print("Perfect beach weather!")

#temperature = 25
#is_sunny = True
#if temperature > 20 and is_sunny:
#  print("Perfect beach weather!")

#username = "Emil"
#password = "python123"
#is_active = True

#if username:
#  if password:
#    if is_active:
#      print("Login successful")
#    else:
#      print("Account is not active")
#  else:
#      print("Password required")
#else:
#  print("Username required")

#score = 22
#extra_credit = 5

#if score >= 90:
#  if extra_credit > 0:
#    print("A+ grade")
#  else:
#    print("A grade")
#elif score >= 80:
#    print("B grade")
#else:
#  print("C grade or below")

#age = 19

#if age < 18:
#  pass
#else:
#  print("Access granted")

#score = 85

#if score > 90:
#  pass
#print("Score processed")

#value = 50

#if value < 0:
#  print("Negative value")
#elif value == 0:
#  pass
#else:
#  print("Positive value")

#def calculate_discount(price):
#  pass is a null operator and is a placeholder for future code

#i = 1
#while i < 6:
# print(i)
#  i += 1

#i = 1
#while i < 6:
#  print(i)
#  if i == 3:
    break
#  i += 1

