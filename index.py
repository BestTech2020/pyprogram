# if 5 > 2:
#     print("Five is greater than two!")
# if 5 > 2:
#  print("Five is greater than two!")
#  print("Five is greater than two!")

# x = 3;#number
# name = "Christopher"
# y=50.55
# str(y)
# sum = x+y
# print(type(name))

# x =""" 
# this is a 
# multiline 
# string"""
# print(x)

# y = " My name is mubarak and I am  this and that"
# for y in "mubarak":
#  print(y)
# print(len(y))

# x = "MUBARAK IS BACK TO THE CLASS WITH, CHAPMAN"
# print("gtb" in x)
# print(x[1:4])
# y = "hearsay"
# print(y.upper())
# print(x.lower())
# ws = "this is an  example of white space"
# print(ws)
# print(len(ws))
# ws = ws.strip()
# print(len(ws))
# print(len(ws.strip()))
# Baracks
# print(x.replace("BARAK", "BARACKS"))
# print(x.split(","))
# y= "mubarak likes peanuts and he is {} and his position in class {}"
# age = 48
# position = 3
# z =x+" "+y
# print(y.format(position,age))

# x = 10
# y=5


# print(x)
# thislist = ("cherry", "apple", "banana", "cherry")
# thislist.sort()
# print(len(thislist))
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# thislist.insert(2, "berry")

# print(thislist.count("cherry"))
# x = ("abc", 34, True, 40, "male")
# print(type(x))
# thisset ={"apple", "banana", "cherry", "apple"}
# thisset.add("mango")
# thisset.discard("cherry")
# print(thisset)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.setdefault('age'))
# a = 200
# b = 33
# if b >= a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
# print("Number determination")
# a = int(input("Enter a number"))
# if a%2==0:
#    print("This is an even number")
# else:
#     print("This is an odd")

# formula for area of a circle
# pi*r**2
# pi = 22/7
# r = int(input("Enter radius"))
# area=pi*r*r
# print(area)
#


#  1. underweight(<18.5)
#  2. normal(18.5 - 24.99)
#  3. overweight(25-30)
#  4. obese(>30)

# bmi calculator
# print("BMI calculator")
# h = float(input("Enter height in meters"))
# w = float(input("Enter height in Kilograms"))
# bmi = w/(h*h)

# txt = "Your BMI is {} sorry! you are underweight"

# if bmi < 18.5:
#     print(txt.format(bmi))
# elif (bmi>=18.5)and(bmi<=25):
#     txt = " Your BMI is {} hurray! you are normal"
#     print(txt.format(bmi))
# elif (bmi>25)and(bmi<=30):
#     txt = " Your BMI is {} sorry! you are overweight"
#     print(txt.format(bmi))
# else:
#     txt = " Your BMI is {} sorry! you are obese"
#     print(txt.format(bmi))
# i = 1
# while i <= 6:
#   print(i)
#   if i==5:
#     break
#   i += 1
# def x(a,b):
#     # for x in range(0,145,12):
#     return a+b
# print(x(3,8))

# import pygame
# pygame.init()

# win = pygame.display.set_mode((500,500))

# pygame.display.set_caption("First Game")

# x = 50
# y = 50
# width = 40
# height = 60
# vel = 5

# run = True
# while run:
#     pygame.time.delay(100)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
    
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x -= vel
#     if keys[pygame.K_RIGHT]:
#         x += vel
#     if keys[pygame.K_UP]:
#         y -= vel
#     if keys[pygame.K_DOWN]:
#         y += vel
#     win.fill((0,0,0))

    
#     pygame.draw.rect(win, (0,255,0),(x,y,width,height))
#     pygame.display.update()
# pygame.quit

#Exercise
#  Print First 10 natural numbers using while loop
#  Print multiplication table of given number

# import pprint

# def solve(bo):
#     find = find_empty(bo)
#     if find:
#         row, col = find
#     else:
#         return True

#     for i in range(1, 10):
#         if valid(bo, (row, col), i):
#             bo[row][col] = i

#             if (solve(bo)):
#                 return True
            
#             bo[row][col] = 0
#     return False

# def valid(bo, pos, num):
#     # Check row
#     for i in range(0, len(bo)):
#         if bo[pos[0]][i] == num and pos[1] != 1:
#             return False
    
#     # Check column
#     for i in range(0, len(bo)):
#         if bo[i][pos[1]] == num and pos[1] != 1:
#             return False
    
#     # Check box
#     xbox = pos[1]//3
#     ybox = pos[0]//3

#     for i in range(ybox*3, ybox*3 + 3):
#         for j in range(xbox*3, xbox*3 + 3):
#             if bo[i][j] == num and (i, j) != pos:
#                 return False

#     return True

# def find_empty(bo):
#     for i in range(len(bo[0])):
#         for j in range(len(bo[0])):
#             if bo[i][j] == 0:
#                 return (i,j)        
#     return None

# def main():
#     board = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#     ]

#     pp = pprint.PrettyPrinter(width=41, compact=True)
#     solve(board)
#     pp.pprint(board)

# main()

# Loops
# i = 1
# while i < 11:
#   print(i)
#   i += 1

# i = 1
# x=int(input("Enter a number to display the multiples"))
# while i <= 12:
#   print(i*x)
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for y in "mubarak":
#     print(y)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# for x in range(4):
#   print(x)
# for x in range(2, 6):
#   print(x)

# for x in range(2, 30, 3):
#   print(x)

# for x in range(2, 25, 2):
#   print(x)
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# def my_function():
#     print("Hello from a function")

# my_function()

# def my_function(fname,lname,nname):
#   print(fname +" "+ lname+ ' '+nname )

# my_function("Emil","tobi")
# my_function("Tobias")
# my_function("Linus")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def one():
#   two()

# def two():
#   three()

# def three():
#   four()

# def four(*bio):
#   print("Today is friday")

# one()

# print("CBT WITH PYTHON")
# score = 0
# name = input("Enter name\n") 

# def question_one():
#       q1=input("How many loops do we have in Python? \nA. One \nB. Two \nC. for \nD. while\n")
#       q1=q1.upper()
#       global score 
#       if q1=="B":
#         print("correct")
#         score = score +1
#       elif q1=="A" or q1=="C" or q1=="D" :
#         print("incorrect")
#       else:
#         print("Invalid input")
#       return score
# question_one()

# def question_two():
#       q1=input("len() in python is equivalent to length in JavaScript? \nA. False \nB. No Idea \nC. True \nD.I don't know\n")
#       q1=q1.upper()
#       global score 
#       if q1=="C":
#         print("correct")   
#         score = score +1   
#       elif q1=="A" or q1=="D" or q1=="B" :
#         print("incorrect")
#       else:
#         print("Invalid input")
#       return score  
# question_two()


# def question_three():
#       q1=input("How many languages do you code? \nA. One \nB. Three \nC. All \nD. Two\n")
#       q1=q1.upper()
#       global score 
#       if q1=="D":
#         print("correct")
#         score = score +1
#       elif q1=="A" or q1=="C" or q1=="B" :
#         print("incorrect")
#       else:
#         print("Invalid input")
#       return score
# question_three()

# print("Mr.", name, "Your score is: ", (score*100)/3, "%" )

print("Welcome to LCI Bank")
def transfer():
  bank=int(input("Select Bank \n1. GTB \n2. UBA \n3. Zenith\n"))
  if bank==1 or bank==2 or bank==3:
    acct_num=int(input("Enter Accout Number"))
    amount()
  else:
    print("Invalid input")
    transfer()

def recharge():
  network=int(input("Select Network\n1. MTN \n2. GLO \n3. Airtel \n4. 9Mobile"))
  if network==1 or network==2 or network==3 or network==4:
    numb=input("Enter your phone Number")
    if len(numb)==10:
      amount()
    else:
      print("Invalid input")
      recharge()


def display():
  x = int(input("SELECT AN OPTION\n1.Withdraw\n2.Transfer\n3.Airtime recharge\n"))
  if x==1:
    withdraw()
  elif x==2:
    transfer()
  elif x==3:
    recharge()
  else: 
    print("Invalid option")
    display()



def withdraw():
  account_type = int(input("select account type\n 1. Current \n 2. Savings"))
  if account_type==1 or account_type==2:
    print("Amount fxn")
    amount()
  else:
    print("Invalid Input")
    withdraw()


def amount():
  amt=int(input("Select amount\n1. 1000\n2. 2000\n3. 5000\n4. 10000"))
  if amt==1 or amt==2 or amt==3 or amt==4:
    print("Transaction Processing...")
    print("")
    print("Transaction Successful")
    print("")
    print("Thank You for Banking with us")
  else: 
    print("Invalid Input")
    amount()

def pin():
  pin = input("Kindly enter your pin\n")
  if len(pin)==4:
    print("pin validated")
    display()
  else:
    print("incorrect Pin")
    exit()

pin()





