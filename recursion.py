# recursion 
"""def display(num):
    if num>10:
      return
    print(num)
    display(num+1)  #function calling itself 
display(1) """

#factorial using recursion.
"""def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)   # Recursive call

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
"""

def factorial (num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(5)) 

#lamda  ,args ,kwags     function after 
