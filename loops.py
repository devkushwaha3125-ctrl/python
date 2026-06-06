
# for i in range(50,121,1):
#     print(i)

# for i in range(-10,31,1):
#     print(i)

# for i in range(10,-21,-1):
#     print(i) 


# for i in range(100,-1,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)
# a = int (input("which number table you want:"))
# for i in range(a,a*10+1,a):
#     print(i)

# for i in range(1,11):
#     if i == 3:
#         break # break will stop all the itrration
#     print (i*10)

# for i in range(1,11):
#     if i == 3 or i==5: 
#         continue # tis will stop only one parcticular itrration
#     print (i*10)

# if break will run else not run 
#if break  not run else will run
# for i in range(1,11):
#     if i == 20:
#         break 
#     print (i*10)
# else:
#     print("i will win")

#question no 1
# n =int(input("enter your number:"))

# for i in range(n):
#     print("hello world") 

#question no 2
# n = int(input("enter your no:"))

# for i in range(1,n+1):
#     print(i)

#question no 3
# n = int(input("enter your no:"))

# for i in range(n,0,-1):
#      print(i)

#question no 4
# n = int(input("enter your no:"))

# for i in range(1,11):
#      print(f"{n} x {i} = {n*i} ")

#question no 5
# n = int(input("enter your no:"))
# sum=0
# for i in range(1,n+1):
#      sum = sum+i

# print(sum)

#question no 6
# n = int(input("enter your no:"))
# fact=1
# for i in range(1,n+1):
#      fact = fact * i
     
# print(fact)


#1count even and ood numbers within a range
# n =int(input("enter your no:"))

# evenno =0 
# oddno =0
# for i in range(1,51):
#     if i%2==0:
#      evenno += 1#shorthand operators  
# else:
#     oddno += 1
#     print(evenno)
#     print(oddno)  


#2count vowels from a string

# s ="hello sherry"
# count = 0 
# for i in s:
#     if i in "aeiouAEIOU":
#         count = count + 1

# print(f"count of vowels are :{count}")  


#you have a range from 1 to 20 you have to print numbers  that are only divisible by 3 and 5

# for i in range(1,21):
#     if  i%3 ==0 and i%5 ==0:
#         print(i) 

#factorial number
# num =10 
# for i in range(1,num+1):
#     if num %i ==0:
#         print(i)
#count numbers of factorial

# num =10 
# count =0
# for i in range(1,num+1):
#     if num %i ==0:
#         count+=1
# print(count)


#prime numbers -> factorial -> and number itself
# num =10 
# count =0
# for i in range(1,num+1):
#     if num %i ==0:
#         count+=1

# if count == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number") 

#sum of factorial 
# num =10 
# sum =0
# for i in range(1,num+1):
#     if num %i ==0:
#         sum +=i 
# print(sum) 
 
#print prime numbers from 1 to 50
# prime numbers -> jinke factors 2 ho (1 and number itself)
# for i in range(1,51):

# for j in range(1,num+1):
#     if num %i ==0:
#         count+=1

# if count == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number") 


# question no 7
# num = 1024
# num2 = str(num) 
# for i in num2:
#     print(i) 

# while loop -> jab tak condition true hai tab tak loop chalega
#we have to make while condition false at some point othrwise it will become infinite loop
# i=0
# while i < 11:# jab tak condition true,while will keep executing.
#     if i==5:
#      break# this is a break statement which is used to exit the loop when the condition is made
#     print(i) 
#     i = i + 1

#question no 1
# num = 1054
# while num >0:
#    print(num%10)#lat digit ko print kar dega 
#    num = num//10 #last digit ko remove kar dega 
# print("num is ",num) 

# num = 1054
# sum = 0
# while num >0:
#    last = num%10  
#    sum = sum + last
#    num = num//10 
# print("num is ",num)  


#que no 2
#check a number is palindrome or not 

# n = 1221
# copy=n
# reverse=0
# while n>0:
#     last=n%10
#     reverse=reverse*10+last

#     n=n//10

# if reverse==copy:
#     print(f"{copy} it is palindrome")
# else:
#     print(f"{copy} its not palindrome") 

