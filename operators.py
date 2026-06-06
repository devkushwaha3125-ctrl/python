# age = 24
# name = "harsh"

# #1st way to use variables
# print("hello your name  is",name,"and your age is",age)
# #2nd way to use variables
# print(f"hello your name is {name} and your age is {age}")


#you have to convert the datatypes while taking the inputs
# age = int(input("Enter your age:"))
# name = input("Enter your name:")
# print(f"your age after 6 year will be {age+6}")
# print(f"your name is {name} and your age after 6 years will be {age+6}")


#take input of rate ,time and calculate simple interest
#Arithmetic operator
# (+,-,/,*,//,%,**)
# a=50
# print(20+20+30) # this is addition operators 
# print(a-10) # this is subtraction operator

# print(int(20/5)) #this is division operator

# print(20//5)# this is floor division operator this will convert value to integer

# print(2*45) #this is multiplication operator

# print(5**4) # this is exponentiation operator this will calulate the power of a number

# print(91%7)# this is modulus operator this will give you the remainder after division

# print(20%5) 

# rate = float(input ("enter the rate of interest:"))
# time = float(input("enter the time :"))
# simple_interest = (rate*time/100)
# print(f"The simple interest is: {simple_interest}")

# p=int(input("enter the principle amount:"))
# r=float(input("enter the rate of interest:"))
# t=float(input("enter the time:"))

# simple_interest=(p*r*t)/100

# print(f"your simple interest will be {simple_interest}")

# p=int(input("enter the principle amount:"))
# r=float(input("enter the rate of interest:"))
# t=float(input("enter the time:"))

# compound_interest = p * ((1 + r / 100) ** t) - p

# print(f"your compound interest will be {compound_interest}")

#comparison operators
# (==,!=,>,<,<=,>=)

# a=12
# b=30

# print(a==b) 

# print(12==12)
# print(12!=12)
# print(20!=20.1)

# print(12<90)
# print(80>40)

# print(12>=12)


#logical operators
# (and,or ,not)


#and operator
#all the operations must be true if even one of the operator is false then i will return false
# print(12 ==12 and 40>30 and 40!=40 and 23<20 )


# #or operation
# # if all are false then i will provide false even one operator is true i will provide true
# print(12!=12 or 30<20 or 12 ==12)
# print(12!=12 or 30<20 or True)

# #not operator
# # i will convert true to false and false to true
# print(not 20==20)

# print((12==12 and 34!=56)and (not bool("hello") or 20!=40))



#assignment operators
#(=,+=,-=,*=,/=)

# a=10
# a=a+30
# a=a+20
# print(a)

# a =0
# a+=1
# a+=2
# a+=3


# a=1
# a *=1
# a *=2


#conditional statements
# age = int(input("tell your age:"))

# if age >= 18:
#     print(" you can vote")
# else:
#     print("you cannot vote")

# money = int(input("mummy paise do:"))

# if money == 10:
#     print("mai jaa rha chips khane")
# elif money == 50:
#     print("kinder joy khau ga")
# elif money == 100:
#     print("pizza kha rha mai")
# else:
#     print("kapde le rha mai") 

# accept the two numbers and print the gretest number
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))

# if num1 >num2:
#     print(f"the greatest number is {num1}")
# else:
#     print(f"the greatest number is {num2}")

#     if num1>num2:
#         print(f"{num1} is greater than {num2}")
#     elif num1<num2:
#         print(f"{num2 } is greater than {num1}")

#     else:
#         print ("both are same")

#question 2
# gen = input("Tell your gender(m/f):")

# if gen == "m" or gen == "M":
#     print("good morning sir")

# elif gen == "f" or gen == "F":
#     print("good morning mam")

# else:
#     print("invalid gender") 

# # QUESTION 3
# num = int(input("enter the number:"))
# if num%2==0:
#     print("the number is even")
# else:
#     print("the number is odd") 


  # Accept name and age — check if the user is a valid voter (18+).

# name = input("enter your name:")
# age = int(input("enter your age:"))

# if age >= 18:
#       print(f" hello {name} you area valid voter.")
# else:
#  print(f" hello {name} you are not a valid voter.")
# print(f"you can vote after {18-age} years")


#Accept a year and check if it is a leap year.


# year = int(input("enter the year:"))
# if (year % 4 ==0 and year % 100 !=0) or (year %400 ==0):
#     print(f"{year}is a leap year")
# else:
#     print(f"{year}is not a leap year")

# year =int(input("tell your year:"))
# if year %100 ==0 and year %400 ==0:
#     print("leap year")
# elif year %100 !=0 and year %4==0:
#     print("leap year")
# else:
#     print("not a leap year")

    #Accept temperature in °C and print a description.
# temp = float(input("enter the temperature in °C: "))
# if temp  >=-5 and temp <=-10:
#     print("freezing cold")
# elif temp >=11 and temp <=25:
#     print("plesant temprature")
# elif temp >=26 and temp <=40:
#     print("hot temprature")
# elif temp >= 41 and temp <=60:
#     print("very hot temprature")
# else:
#     print("not in range") 


#take 3 inputs and 
# a =int(input("enter the first number:"))
# b =int(input("enter the second number:"))
# c =int(input("enter the third number:"))

# if a ==b and b==c:
#     print("all are equal")
# elif a == b or b == c or a==c:
#     print("two numbers are equal")
# else:
#     print("none are equal")



# char  = input("enter the char:")
# if  char in "aeiouAEIOU":
#     print("the char is vowel")
# else:
#     print("the char is consonant")
    


