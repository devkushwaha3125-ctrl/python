#Sets 
"""
 empty sets->{},set()  
values in sets cannot be duplicate.
sets are unorderd  or not subscriptable .
sets are hetrogenous 
mutable.
"""
"""
s = {}  #empty set
print(type(s))  


s = set()
print(type(s)) """



# s ={1,2,3,4,5}   sets are seaperated by coomas
# print(type(s)) 

# values in sets cannot be duplicate
"""s = {1,1,2,2,3,4,5,5}
print(s)"""

# sets are unorderd  or not subscriptable 
"""s = {1,1,2,2,3,4,5,5}
print(s[4]) """


# sets are hetrogenous 
"""s={'hello',1,3,3.14,True}
print(s)"""

# item assenginment is not allow and iteam adding is allow


#Methods in sets

#1. add a new value in set
# item adding
"""s={1,1,1,1,2,2,3,3,4,4,5,5}
s.add(100) #adding single value in set
print(s)



s={1,1,1,1,2,2,3,3,4,4,5,5}
s.update([200,300,400,500])  # adding multiple values inside  set
print(s) """

#2. Removing an element from the set
#1. remove(element)
"""s={1,1,1,1,2,2,3,3,4,4,5,5}
s.remove(1)   # this will remove the element 
s.discard(6)  # if value exist nahi karti toh it will return you exact set bina kisi error ke 
print(s)"""


"""s={1,1,1,1,2,2,3,3,4,4,5,5}
s.clear() #it will remove all the elements 
print(s)"""


#advance methods in sets.
"""
1. Union  -> sare elements between your sets
2. Intersection -> dono set ke beech mai jo common values
3. difference -> s1 mai ho par s2 me na ho
4. symmetric difference -> common elements ko chodh ke jo bach rhe wo la do.

"""
#union
"""s1 ={1,2,3,4,5}
s2 = {1,6,7,8}
print(s1.union(s2))"""


#intersection
"""s1 ={1,2,3,4,5}
s2 = {1,6,7,8}
print(s1.intersection(s2))

"""
#difference
"""s1 ={1,2,3,4,5}
s2 = {1,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1)) """

#symmetic difference  
"""s1 ={1,2,3,4,5}
s2 = {1,6,7,8}
print(s1.symmetric_difference(s2))"""


"""
l =[1,2,1,2,1,3,3,3,4,5,6,7]
s= set()
for i in l:
    s.add(i)
print(s)"""

















