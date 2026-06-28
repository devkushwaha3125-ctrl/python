#Dictonary
#[] -> list
# {} -> curly brackets dictionary 

"""
key - values  pairs
keys cannot be duplicate
but values can be duplicate
1. hetrogenous
2.mutable
3.ordered

"""

"""
d= {'a':10,'b':20,'c':30,'d':40}
#print 40
print(d['b']) 
"""

# creating a new key and assigning value to it.
"""
d['e' ]= 100 
print(d) 
"""


"""
d= {'a':10,'b':20,'c':30,'d':40,'e':100}
d['e'] =200 # old value at key 'e' will be overwrite 
print(d) 
"""

"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
"""
#1. age -> 25
"""
info['age'] = 25 #item assigenment
print(info)
"""

#Methods in dictionary 
#1. .values()  ->sirf dictionary ki values
"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}

print(info.values())
"""

#2.  .keys() -> sirf keys milegi 
"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
print(info.keys())
"""


#3.  .items() -> to print both the values
"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
print(info.items())
"""

#4.  .pop()  -> it accepts key and remove key and value
"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
info.pop('name') 
print(info)
 """


"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
print(len(info))# it will give the length of the dictionary jitne keys utni length 
""" 

"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
for i in info: #i->keys
    print(i,info[i]) #info [i] -> values
"""


"""
info ={'name':'rahul','age':21,'marks':50.25,'present':True}
#you will only get values from dictionary 
for i in info.values():
    print(i)
"""

#5. .get() - > gives you value of a key and if not present gives you None
"""
d ={'a':10,'b':20,'c':30}

print(d.get('d'))  
"""


#6.  .update({key:value})  ->  it updates the value in dic
"""
d ={'a':100,'b':200,'c':300}
d.update({'c':500})
print(d)
"""

#7.      .clear()  -> removes all the elements 
"""
d ={'a':100,'b':200,'c':300}
d.clear()
print(d)
"""
# del d  # delete permanent 
# print(d)


#question of dictionary 

#1. we have two list and we have to make list1 as key of dictionary and list2 as value


"""
l1 =['a','b','c','d']
l2 =[10,20,30,40] 

d={}

for i in range(len(l1)): # i 0123
    d[l1[i]] = l2[i]
print(d)
"""


#2. you have a list make the indexs as the key and elements present on those indexes as value
# 0,1,2,3,4 -> keys
"""l=[10,20,30,40,50]

d={}
for i in range(len(l)):
    d[i]= l[i]
print(d) 
     """

#3. merge 2 dictionaries
"""d1 = {'a':10,'b':20}  # c:30,d:40
d2 = {'c':30,'d':40}

for i in d2: # i -> c,d
    if i not in d1: #c is not in d1
        d1[i] = d2[i]
print(d1) 


d1 = {'a':10,'b':20}  # c:30,d:40
d2 = {'c':30,'d':40}
d1.update(d2)"""


#4. frequency count
"""l =[1,1,1,2,2,3,3,6,6,7,6,3,4,1,2]
d={} 
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)  
"""



