"""
Data Structure(advance data type)
1. List
2. dictionary
3.tuples
4.set


"""

#1.List
"""
Denoted by -> []  square brackets
1. hetrogenous data structure - multiple type ke data ko store krwa skste hai
2.DUPLICACY IS ALLOWED
3. list is ordered 
4.mutable -> we can change the value of the item in the list
"""
# l =[] empty list
"""l =[10,20,30,40,50]
print(l)
print(type(l)) 

l =[10,"name",True,3.14] """

"""l=[10,30,303,40,50]
print(l[3])"""

"""l=[10,30,303,40,50]

l[3] =400 # item assigenment 
print(l)"""

# l=[5] ==100 index out of range


"""l=[10,30,303,40,50]"""
#item wise loop
"""for i in l:
    print(i)"""

#index wise loop
"""for i in range(len(l)): # i->0,1,2,3,3
    print(i, l[i]) """

    #i-> index of list
    #l[i] -> item at index 


""""l = [1,67,10,25,14,77]

for i  in range(len(l)):
    if l[i]  > 15:
     print( i, l[i] ) 
""" 
# sum all the elements of the list
"""l= [10,20,30,40,50]
sum=0
for i in l:
    sum = sum +i
    print(i) 
print(sum)"""


#slicing 
# [start=0:stop-1:step=1]
# l = [10,20,30,40,50]
# print(l[1:4:1]) #string

# l = [10,20,30,40,50]
#methods in list

#1.  .append() -> adding element at the last of list 
"""l = [10,20,30,40,50]
l.append(100)
print(l)"""

#2.  .extend() -> adding multiple element at the last of list 
"""l1 = [10,20,30,40,50]
l2 = [60,70,80]
l1.extend(l2)
print(l1)"""

#3.  .insert(index,value)  -> this will insert the value in list
"""l1 = [10,20,30,40,50]
l1.insert(1,100)
print(l1)"""

#4.  .pop(index) -> this will remove the value you want to remove
"""l1 = [10,20,30,40,50]
l1.pop(1)
print(l1)"""

#5.  .remove(element) 
"""l1 = [10,20,30,40,50]
l1.remove(5) # agar duplicate value hai toh first occurence remove.
print(l1)"""


#6.   len () -> list length 
"""
l1 = [1,5,5,5,5,2,3,4,5]
print(len(l1))
"""


#Enumerate  ->  list -> [10,20,40.50]  -> index -> 0,1,2,3,4
#enumerate  ->  index ke sath unki values bhi dega  
"""
l = [10,20,30,40,50]
for index , value in enumerate(l):
    print(index,value) 

for index , value in enumerate(l):
    print(index+1,value) 
"""

#question no 1
#Accept List elements and reprint it.
#part 1 accept elements
"""n= int(input("enter the size of the list:")) #5
l = []
for i in range(n): 
    element= input(f"enter element {i}for your list:")
    l.append(element)
print(l) """

#question no 2
#Print  List elements in reverse order / reverse the list without using slicing
"""lst = [1, 2, 3, 4, 5]

rev = []

for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])

print(rev)"""


#question no 3
# Print positive and negative elements of an List
"""
l =[ 1,3,-5,-6,23,-3]
neg =[]
pos =[]

for i in l:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
print(neg)
print(pos) """



#Bubble sort
"""l =[1,5,3,7,4,10]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j] :
            l[i],l[j] = l[j],l[i] # swapping 
print(l)"""


# for i in range(5):
#     print("hello world") 
#brute force 

#online extra 
#question no 1
# largest element from a list
"""l=[2, 96, 69, 77, 145, 20] 
max = l[0] #2
for i in l:
    if i > max :
        max =i
print(max)"""


#index
"""l=[2, 96, 69, 77, 145, 20] 
max = l[0] #2
index = 0 #4
for i in range(len(l)):
    if l[i] > max :
        max =l[i]
        index = i
print(f"max element from the list is {max} and at index {index}")"""


#question no 2
# Mean of List elements.

"""l = [1,5,6,8,9] 

sum =0 
for i in l:
    sum= sum+i
print(sum/len(l)) """


# 
"""
l=[10,5,20,15]
largest = l[0] #20
s_largest = l[0] #15

for i in l: #i->15
    if i>largest: # 15>20
        s_largest = largest
        largest = i

    elif i>s_largest: #15>10
        s_largest=i
print(largest,s_largest) """



# index


"""l=[10,5,20,15]
largest = l[0] #20
s_largest = l[0] #15

index =0 #2
sindex =0#0

for i in range(len(l)): #i->2
    if l[i]>largest: # 20>10
        s_largest = largest
        largest = l[i]

        sindex=index
        index = i
           
    elif i>s_largest: #15>10
        s_largest=l[i]
         
print(largest,s_largest) """


#question no 4
# plaindrome or not
#method 1
"""l= [1,2,2,1]
rev_l = []


for i in range(len(l)-1,-1,-1):
    rev_l.append(l[i])

if l == rev_l:
    print('list is palindrome ')
else:
    print('list is not palindrome') 
"""

    # method 2 
"""l = [1,2,2,9]

for i in range(len(l)):  #i->0
    if l [i] != [len(l)-1-i]: #l[0] != l[4-1-0] -> 1!=9
        print('not palindrome')  #print
        break
else:
    print('list is palindrome')"""



"""l = [1,2,2,1]
rev_l = []

for i in range(len(l)-1,-1,-1):
    rev_l.append(l[i])

if l == rev_l:
    print('list is palindrome')
else:
    print('list is not palindrome')"""


"""
l= [1,2,2,9]

for i in range(len(l)):
    if l[i] != [len(l)-1-i]:
        print('not palindrome')
        break
else:
    print('is palindrome')
"""


#question  
"""
l =[1,2,3,4,5]
l2 = [1,3,4,5,6] 

new = []  #common elements rakhne hai 

for i in l:
    for j in l2:
        if i == j:
            new.append(i)

print(new)
"""

# ques. you have a list [1,2,3,4,5] and you have a variable k=2 and
#  you just have to rotate the list by k elements
"""
l=[1,2,3,4,5]
k=2
for i in range(k):
    last =l[-1]  #storing value of the list
    for j in range(len(l)-1,0,-1):
        l[j] = l[j-1]
    l[0]=last
print(l)
     """             

# you  have a list  [1,1,1,2,2,3,3,4,4,5,5,5.6] frequency count
"""
l= [1,1,1,2,2,3,3,4,4,5,5,5.6]
d={}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
 """
# 
"""
d = {}
for i in d:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
print(d) 
"""
















