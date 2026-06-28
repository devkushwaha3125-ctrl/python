
# problem no 


nums=[3,2,3,2,2,2]

#3->2->(3,3)  2/2=0 pair 
#2->4->>(2,2) (2,2)  4/2=0 pair
#every element is making a pair 
#no some elements are not maling pair 

d={}  # {3:2,2:4}
for i in nums: #i->3
    if i not in d:
        d[3] = 1
    else:
        d[i] +=1


#itni loop jisse i ke andar sirf values aaye
for i in d.values():
    if i %2 !=0: #1 pair -> 2 elements 
        print('not making pair')
        break
    else:
        print('making pair')


# factorial using recursion
# print prime number within a range 



