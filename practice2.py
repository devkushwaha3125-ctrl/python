#question no 1
#print the numbers from given input by using recursion
"""def display(num):
    if num >10:
        return
    print(num)
    display(num+1)
display(1) 
"""

# question no 2
# print factorial of number by recursion
"""def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
num =int(input("enter your number:-"))
print("Factorial =", factorial(num))



def factorial(n):
if n==0 or n==1:
return 1
return n*factorial(n-1)
num = int(input("enter your number:-))
print("factorial=",factroial(num))




def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
num = int(input("enter your number:-"))
print("factorial=",factorial(num))"""

#question no 1
#print hello world n time
"""n=int(input("tell your number:-"))
for i in range(n):
    print(f"hello world") """

"""n = int(input("tell your number:-"))

for i in range(n):
    print(f"{i} :- Hello World")"""

# """question no 2
# print numbers from 1 to n """
"""n = int(input("tell your number:-"))

for i in range(1,n+1):
    print(i) """


#question no 3
#print the numbers from nto1
"""
n = int(input("tell your number:-"))

for i in range(n,0,-1):
    print(i) 

n = int(input("tell your number:-"))

for i in range(n,0,-1):
    print(i) """

# question no 4
# summ of natural numbers (1to n)

"""n = int(input("tell your number:-"))
sum=0
for i in range(1,n+1):
    sum += i
print(sum) """

#question no 5
#print factorial of number
"""n = int(input("tell your number:-"))
fact=1
for i in range(1,n+1):
    fact *= i
print(fact) """

#question no 6
#sum of even & odd number in range
"""n =int(input("enter your number:-"))

even_sum = 0
odd_sum = 0

for i in range(1,n+1):
    if i % 2==0:
        even_sum += i
    else:
        odd_sum += i

print(f"even sum = {even_sum} and odd sum = {odd_sum}")
"""

"""n =int(input("number:="))

even_sum = 0
odd_sum = 0

for i in range(1,n+1):
    if i%2==0:
      even_sum+=i
    else:
       odd_sum += i
print(even_sum,odd_sum)"""

#question no 7
# pirnt all factors of a number
"""n =int(input("enter your number:-"))

for i in range(1,n+1):
    if n%i==0:
        print(i) """

"""n = int(input("entre your number:-"))

for i in range(1,n+1):
    if n%i==0:
        print(i)"""

# question no 8
# sum of all factors
"""n = int(input("entre your number:-"))
sum =0
for i in range(1,n+1):
    if n%i==0:
        sum+=i
print(sum) """

#question no 9
#power calculation (a^b)
"""a = int(input("tell your value:-"))
b = int(input("tell your exponent:-"))

power = a 
for i in range(b-1):
    power = power * a

print(f"after power your answer is {power}") """
"""
a = int(input("tell your value :-"))
b = int(input("tell your value:-"))

power = a
for i in range(b-1):
    power = power * a

print(f"after power your answer is {power}") """


#question no 10
# print prime number check 
"""n = int(input("give your number (prime check):-"))
count = 0

for i in range(1,n+1):
    if n % i ==0:
        count= count+1

if count == 1:
    print("your number is unity number")
elif count == 2:
    print("your number is prime")
else:
    print("your number is composite")
    """
"""n = int(input("give your number (prime check):-"))

for i in range(2,n):
    if n% i ==0:
        print("sorry your number is composite")
        break
else:
    print("your number is prime")"""



#questions of list
#question no 1     #Accept List elements and reprint it.
"""n =int(input("enter the size of the list :"))
l=[]
for i in range(n):
    element= input(f"enter element {i}for the list")
    l.append(element)

print(l) 


n= int(input ("enter the size of the list:"))
l=[]
for i in range(n):
    element = input(f"enter the element{i} for the list")
    l.append(element)

print(i) """


#while looop questions
# question no 1
# print each digit (reverse order)

"""a =int(input("please tell  your number"))

while a>0:
    print(a%10)
    a=a//10 


a= int(input("enter your number:-"))

while a>0:
    print(a%10)
    a=a//10 """


# question no 2
# sum of all digits

"""
a= int(input("enter your number:-"))
s=0
while a>0:
    s = s+a%10
    a=a//10 

print(f"your digits sum is {s}")"""

"""
a =int(input("enter your number:-"))

s=0
while a>0:
    s= s + a % 10
    a = a//10 
    
print(f"your sum is {s}")"""


#question no 3
# reverse a number
"""
n =int(input("enter your number:-"))
rev =0
while n > 0:
    rev = rev * 10 + n%10 
    n = n//10

print(f"your number reverse is {rev}") """



"""n =int(input("enter your number :-"))

rev = 0
while n > 0:
    rev = rev  * 10 + n %10
    n = n // 10
print(f"your number reverse number is {rev}") """ 


#question no 4
# palindrome number check 

"""a = int(input("please tell your number ") )

copy = a
rev =0 
while a>0:
    rev= rev* 10 + a%10
    a =a//10

if rev == copy:
    print("yes your number is palindrome ")
else:
    print("sorry your number is not palindrome")"""

"""
a =int(input("entr your number :-"))

copy =a 
rev=0
while a>0:
    rev= rev*10 +a%10
    a=a//10

if rev==copy:
 print("the number is palindrome")
else:
   print("the number is not palindrome")"""

#question no 5
# automorphic number
"""
a =25
dup = a
square = a ** 2 #625
count =0 
while a>0:
    count =count +1
    a= a//10


extract = square % (10**count) 

if extract == dup:
    print("your number is automorphic")
else:
    print("sorry your number is not automorphic")


a= 25 
dup =a
square = a**2
count =0
while a>0:
    count = count +1
    a= a//10

extract = square % (10**count)

if extract == dup :
    print("numbeer automorphic")
else:
    print("number not automorphic")
"""

"""a= 25 
dup = a
square = a**2
count = 0
while a>0:
    count = count+1
    a =a//10

extract = square % (10**count)

if extract == dup :
    print("number is automorphic")
else:
    print("number is not automorphic") """


