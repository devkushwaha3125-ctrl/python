#print string in reverse ,its length 

# name ="Mohit"
# print(name[::-1])
# print(len(name))
# print(name.upper())
# print(name.lower()) 

# name = "PyTHon"
# lower=""
# upper=""
# for i in name:
#     if i.islower():
#         lower = lower+i
#     else:
#         upper = upper + i
# print(lower+upper) 


# String Questions:
# Q. Print string in reverse, its length, in uppercase, lowercase and copy into another string
# a = input("Enter Your String")
# s= (a[::-1])
# print(s)
# print(len(a))
# print(a.upper())
# print(a.lower())

# mame = "pyThon"
# lower = ""
# upper  = ""
# for i in mame:
#     if i.islower():
#         lower = lower + i
#     else :
#         upper = upper + i
# print(lower + upper)

# Q. Write a program to enter a no. from user and check whether it is armstrong number or not.(jiska sum of cubes of digits is eqaul to the number ex : 153 = 1^3+5^3+3^3 = 153(Armstrong number)).
# n = int(input("Enter Your Number"))
# copy = n
# power = len(str(n)) #
# sum = 0

# while n > 0 :
#     last = n % 10
#     sum = sum + last**power
#     n = n // 10

# if copy == sum:
#     print(f"{copy} is a Armstrong Number")
# else:
#     print(f"{copy} Number is not a Armstrong")

# Q. Write a program to enter a no. from user and check whether it is perfect number or not.
# n = int(input("Enter your Number-:  "))
# sum = 0
# for i in range(1,n-1):
#     if n % i == 0:
#         sum = sum + i
# if n == sum:
#     print("Number is Perfect Number")
# else:
#     print("Number is not Perfect")

