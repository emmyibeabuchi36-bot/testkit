print("Hello, welcome to class today",)
print("Rice", "Beans", "Palm oil")
print("Rice, Beans, Palm oil")
print("Rice", "Beans", "Palm oil", sep=" | ")
print("IEM,",end="")
print("open swiss bank")
print("Appoint my niggas as ministers")
print("Continue from where Tinubu stoped")
print("Repent and become a reverend father")
# this is for seperation and listing
print('Rice\t1200\nBeans\t900\npalmoil\t1500')
print(0.1+0.2)
# this is for raised to power and in python, computer calculates from the right to the left  (3^2)= 9  (2^9)=512ans
print(2**3**2)
hour= 7
minute = 45
journey = 260
total = hour * 60 + minute + journey
print("arives at", (total// 60)% 24, ":", total % 60, sep="")
print((725//60),":", (725)%60)
# how to pass and print a variable
n1 = 1
n2 = 2
total =(n1+n2)
print(total)
# how to ask a question
# name = input("what your name?")
# print("good afternoon," + name)

# age = input("How old are you?")
# print(age + 1)

# Amout = float(input("How much you wan send?"))
# fee = amount * 0.005
# total = amount + fee
# print("amount" + str(round(amount,2)))
# print("Fee " + str(round(total, 2)))

# BOOLEN AND APPLICATION

power_is_on = False
if power_is_on:
    print("up nepa")
else:
    print("put on the Gen") 

fare = 200
money = 200
if money < fare:
    print("Broke Nigga")
else:
    print("Enter sir!") 
    print("your balance sir is =", money - fare)            

# MULTIPLE IF STATEMENTS
has_fuel = True
has_cash = False
if has_fuel:
    print("Gen can run")
    if has_cash:
        print("get more fuel")
    else:
        print("Manage whats left")
else:
    print("NEPA abeg")   

# grading system  

score = 92
if score >= 75:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 65:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F9"    
print(grade)    

# WHILE LOOP
m = 0
while m < 100:
    m += 1
    print(m)


# WHILE LOOP IN GUESSING GAMES
guess = int(input("guess the secret number: "))
secret = 7
while guess != secret:
    print("wrong, good luck next time")
    guess = int(input("guess the secret number: "))
print("Well done! its 7")    

# Assignment on module 3 pg 30

# FOR LOOP
transaction = (5000, 2000, 10000, 500, 20000)
total = 0
for amount in transaction:
    total= total + amount
    print("Added", amount, "running total", total)
print("Total for today:", total)    

# RANG


# LIST 
names = ["Grace", "Mercy", "Zainab", "Abbas", "David", "Daniel", "Samuel" ]
for name in names:
    print("I am", name)

# when looping through a list and you want it to stop
queue = ("Chidi", "Aisha", "Tunde")
for person in queue:
    if person == "Bola":
        print("Found intruder")
        break
    else:
        print("Bola is not meant to be here") 
# HOW TO READ THE INDEX OF ITEMS IN A LIST mates
mates = ("Chidi", "Bola", "Tinubu", "Ahmed")
# print(mates[0])     
# # HOW TO REPLACE ONE ITEM ON A LIST WITH ANOTHER ITEM
# students = ("Chidi", "Bola", "Tinubu", "Ahmed")
# del students[1]
# print(students)
 
scores = [68, 92, 45, 92, 68, 77]
unique =[]
for score in scores:
    if score not in unique:
       unique.append(score)
print(unique)   
           
