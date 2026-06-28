#some advanced functions.


"""
*args -> accetps arguments in form of tuples

"""



"""def add(*chacha):  # 10,20,30
    print(chacha)

add(10,20,30)"""

"""
def add(*chacha):  # 10,20,30
    sum=0
    for i in chacha:
        sum += i
    return sum

print(add(10,20,30))"""

"""
kwargs -> dictionary  me hi data lega and return bhi dictionary me karwata hai

"""

"""def info(**details):
    print(details)
info(name="chacha",age=40,gender="m",address="Bhopal",wife="chachi")"""

"""
def info(**details):
    for key ,value in details.items():
     print(key,value)
info(name="chacha",age=40,gender="m",address="Bhopal",wife="chachi")"""


"""
lambda -> too write code in one line 

"""

"""add = lambda a,b : a+b
print(add(10,20)) """


# make a lambda function which accepts 2 variable a and b but give output as a^b 2^2=4

"""power = lambda a,b : a**b 
print(power(2,2))"""







