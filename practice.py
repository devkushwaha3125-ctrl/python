# #some datatype in python
# #int datatype
# a = 10
# print(type(a))


# #float datatype
# a = 10/24
# print(type(a))

# #boolean datype
# a=True
# print(type(a))

# #string datatype
# a= "hello dev"
# print(type(a))

#slicing in python
# a= "hello dev"
# print(a[-9:0:7])

#condition statement question
#question 1
# a=int(input("enter your first no:"))
# b=int(input("enter your second no:"))

# if a>b :
#     print(f"{a} is greater than no{b}")
# elif a<b :
#     print(f"{b}is greater than no{a}")

# else:
#     print("both are same") 

# using of arithmetic operator
#question no 1
#calculate simple interest and compount interest

# P = int(input("enter your principle amount:"))
# R = float(input("enter your rate:"))
# T =float(input("enter your time:"))

# simple_interest = (P*R*T)/100
# compount_interest =(P*(1+R/100)**T)-P
# print(f"your simple interest will be {simple_interest}and compount interest will be {compount_interest}")


# P =int(input("enter your principle amount:"))
# R = float(input("enter your rate :"))
# T = float(input("enter your time:"))

# simple_interest =(P*R*T)/100
# compount_interest =(P*(1+R/100)**T)-P

# print(f"your simple interest will be {simple_interest} and compount interest will be{compount_interest}")


# condition statement
#question no 1 accept two no and print the greatest between them

# A = int(input("enter your first no:"))
# B = int(input("enter your second no:"))

# if A > B :
#     print(f"the{A} greater than  {B}")

# elif B > A :
#     print(f"the{B} greatesr than {A}")

# else:
#     print("both number are same")


#question no 2 
#Accept gender from user and print a greeting message.
# gen = input("Tell your gender (M/F):")

# if gen == "M" or gen == "m":
#     print("Good morning sir")
# elif gen =="F" or gen =="f" :
#     print("Good morning mam")

# else:
#     print("invalid gender")

#question no 3
#Accept an integer and check if it is even or odd.
# a = int(input("enter your no:"))
# if a%2==0:
#     print("the no is even")

# else:
#     print("the no is odd")

#question no 4
#Accept name and age — check if the user is a valid voter (18+).
# name = input("enter your name:")
# age = int(input("enter your age:"))

# if age >=18 :
#     print(f"hello {name} you are valid voter")
# else:
#     print(f"hello  {name} you are not a valid voter,you can vote after{18-age} years")



#question no 5
#Accept a year and check if it is a leap year.
# Y = int(input("enter the year:"))
# if Y %100 ==0 and Y % 400 ==0:
#     print(" is leap year")
# elif Y %100!=0 and Y %4 ==0:
#     print ("is leap year")
# else:
#     print("not a leap year") 

#question no 6
#Accept temperature in °C and print a description.
# temp = float(input("tell the temperature:"))

# if temp>=-5 and temp <=-10:
#     print("freezing cold")
# elif temp >=11 and temp <=25:
#     print("pleseant temprature")
# elif temp >=26 and temp <=40:
#     print("hot temprature")
# elif temp >=41 and temp<= 60:
#     print("very hot temprature")
# else:
#     print("not in range")

# For Loop Questions
#Print "Hello World" n times.
# n =int(input("enter your no:"))
# for i in range(n):
#     print("Hello world")

# n = int(input("enter your no:"))
# for i in range(n):
#     print("hello world")


# n = int(input("enter your no:"))
# for i in range (n):
#     print("hello world")

# n = int (input ("enter your no :"))
# for i in range (n):
#     print ("hello world")

# n= int(input("enter your no:"))
# for i in  range(n):
#     print ("hello world")



# n =int(input("enter your no:"))
# for i in range(n):
#     print("hello world")



#question no 2
#Print natural numbers from 1 to n.
# naturalno =int(input("enter your natural no:"))
# for i in range(1,naturalno+1):
#     print(i)

# n = int (input("enter your no:"))
# for i in range(1,n+1):
#     print(i)


# n =int(input("enter your no:"))
# for i in range(1,n+1):
#     print(i)

#question  no 3
#Reverse for loop — print n down to 1.
# n= int (input("enter your no:"))
# for i in range (n,0,-1):
#     print(i)


# n=int(input("enter your no:"))
# for i in range(n,-1,-1):
#     print(i)

# n=int(input("enter your no:"))
# for i in range(n,0,-1):
#     print(i)


#question no 4
#Print the multiplication table of a number.
# n =int(input("enter your no:"))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# n =int(input("enter your no:"))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")


# n= int(input("enter your no :"))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# n=int(input("enter byour no:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")



# n=int(input("enter your no:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

#question no 5
# #Sum of first n natural numbers.
# n=int(input("enter your no:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i

# print(sum) 
# n=int(input("enter your no:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i

# print(sum)


# n =int(input("enter your no :"))
# sum =0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)


# n=int(input("enter your no:" ))

# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)


#question no 6
#Factorial of a number.
# n=int(input("enter your no:"))

# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n=int(input("enter your no:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


# n=int(input("enter your no:"))

# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)




# n=int(input("enter your no:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)






#condition question practice
#que no 1
# num1 =int(input("enter your first no:-"))
# num2 =int(input("enter your second no:-"))

# if num1>num2:
#     print(f"the first no{num1} is greter than second no{num2}")
# elif num1<num2:
#     print(f"the second no{num2} is greter than first no{num1}")
# else:
#     print("both no are same")

#que no 2
# gen = input("enter your gender (m/f):-")
# if gen == "m" or gen=="M":
#     print("good moring sir")
# elif gen == "f" or gen=="F":
#     print("good moring mam")

# else:
#     print("invalid gender")



#     gen == input ("tell your gender:-")
#     if gen=="m"or gen=="M":
#         print("good moring sir")
#     elif gen == "f" or gen =="F":
#         print("good moring mam ")
#     else:
#         print("invalid gender")

#que no 3
# n = int(input("enter your no:-"))
# if n % 2 ==0:
#     print("the no is even")
# else:
#     print("the no is odd")

#que no 4 
# name = (input("enter your name:- "))
# age = int(input("enter your age:-"))

# if age >=18:
#     print(f"hello {name} your are a valid voter ")

# else :
#     print(f" your are invalid voter ,you can vote after{18-age} years") 

#que no 5
# y=int(input("enter the year:-"))
# if y %100==0 and y%400==0:
#     print("it is a leap year")
# elif y%100!=0 and y%4==0:
#     print("it is a leap year")

# else:
#     print("it is not a leap year")

#que no 6
# temp=int(input("enter the temperature:-"))

# if temp>=-5 and temp<=-10:
#     print("freezing cold")
# elif temp >=11 and temp <=25:
#     print("pleseant temperature ")
# elif temp >=26 and temp<= 40 :
#     print("hot")
# elif temp >=41 and temp <=50:
#     print("very hot")
# else:
#     print("invalid temperature ")


#loops question 
#que no 1
# n=int(input("enter the number:-"))
# for i in range(n):
#  print("hello world")

#que no 2
# n = int(input("enter your no:"))

# for i in range(1,n+1):
#     print(i) 

# n =int(input("enter your no :-"))
# for i in range(1,n+1):
#     print(i) 


#que no 3
# n = int(input("enter your no:"))

# for i in range(n,0,-1):
#     print(i)


# n =int (input("enter your no :-"))
# for i in range(n,0,-1):
#     print(i)

#question no 4
# n =int(input("enter the no:"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")


#que no 5
# n =int (input("enter your no:-"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
    
# print(sum)

# n =int (input("enter your no:-"))

# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)  


#que no 6
# n=int(input("enter your no:-"))

# even=0
# odd=0
# for i in range(1,51):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)   


# even=0
# odd=0
# for i in range(1,11):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1

# print(odd)
# print(even)

#que no 7
# n =int(input("tell your no:-"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i) 

#         n=int(input("tell your no :-"))
#         for i in range(1,n+1):
#             if n%i==0:
#                 print(i)



#question no 8
# n=int(input("tell your no :-"))
# sum=0
# for i in range(1,n):
#         if n%i==0:
#          sum=sum+i

# if sum==n:
#      print("perfect number")
# else:
#      print("not a perfect number") 





# n = int (input("tell your number:-"))

# sum=0

# for i in range(1,n):
#     if n%i==0:
#         sum=sum+1

# if sum==n:
#     print("perrfect number ")
# else:
#     print("not perfect number")


#que number 9
# n =int (input("enter your number:-"))

# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1

# if count==2:
#     print("number is  prime")
# else:
#     print("composite number")   

# n=int(input("enter your number:-"))

# count=0
# for i in range(1,n+1):
#     if n%i==0:
#      count+=1

# if count==2:
#    print("prime number")
# else:
#    print("composite numberr")


# que no 10
# n ="python"
# rev=""
# for i in range(len(n)-1,-1,-1):
#     rev=rev+n[i]

# print(rev)



# a="python"

# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev= rev+a[i]

# print(rev)


#queno 11

# a =input("enter your string:-")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]

# if rev==a:
#     print("it is palindrome")
# else:
#     print("not a palindrome")

# a = "naman"

# rev ="" 

# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]

# if rev ==a:
#     print("palindrome")
# else:
#     print("not palindrome")


# que no 12

# a = "P@#yn26at^&i5ve"

# char=0
# spchar=0
# digits=0


# for i in a:
#     if i.isdigit():
#         digits=digits+1
#     elif i.isalpha():
#         char=char+1
#     else:
#         spchar=spchar+1

# print(f"digits are{digits} , char are {char} , spchar are{spchar}") 



# a = "P@#yn26at^&i5ve"

# char=0
# spchar=0
# digits=0


# for i in a:
#     if (ord(i) >= 65 and ord(i) <= 90 or ord(i) >=97 and ord(i) <= 122):
#                 char=char+1
#     elif (ord(i) >= 48 and ord(i) <= 58 ):
        


# while loops question
# question no 1

# n= int(input("enter your number:-"))

# while n>0:
#     print(n%10)
#     n=n//10 


# n=int(input("enter your number:-"))

# while n>0:
#     print(n%10)
#     n=n//10  

#question no 2
# n =1054
# sum=0
# while n>0:
#     last=n%10
#     sum=sum+last
#     n=n//10
# print(n)
 
#question no 3

# n= int(input("enter your no :-"))
# rev=0
# while n>0:
#    rev=rev*10+n%10 
#    n=n//10

# print(rev) 


# n=int(input("enter your number:-"))
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10

# print(rev)


# question no 4

# a=int(input("enter your number:-"))

# copy=a
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10

# if rev==copy:
#     print("palindrome")
# else:
#     print("not a palindrome") 

#function questions
#question no 1print hello world
# def greet(name):  #parameter passkarnege 
#     print(f"hello {name}")
# greet("dev")   #argument denge 

#  que no 2 print greatest between 2 no 
# def greatest():
#     a=int(input("enter your number:-"))
#     b=int(input("enter your number:-"))

#     if a>b:
#         print(f"{a} is greater number than {b}")
#     elif b>a:
#         print(f"{b} is gerater number than {a}")
#     else:
#         print("both numbers are equal")
# greatest() 


# reverse a string using function
# def palindrome(name):
#     reverse=name[::-1]
#     if name == reverse:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome("madam")

a = "python"

print(a[-1::])
