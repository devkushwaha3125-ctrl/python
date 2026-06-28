# Q1. Factorial Using Recursion
# Write a Python function to find the factorial of a given number using recursion.
# Sample Input
# Enter number: 5
# Sample Output
# Factorial = 120


"""
def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
num =int(input("enter your number:-"))
print("Factorial =", factorial(num)) 
"""

# Q2. Prime Numbers in a Range
# Write a Python program that accepts two numbers and prints all the prime numbers between them.
# Sample Input
# Enter starting number: 10
# Enter ending number: 30
# Sample Output
# 11, 13, 17, 19, 23, 29
"""
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=" ")"""


# Q3. Count Vowels Using Function
# Write a function that accepts a string and returns the total number of vowels present in it.
# Sample Input
# Enter string: Programming
# Sample Output
# Total vowels = 3

"""
def vowels(word):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in word:
        if ch in vowels:
            count += 1

    return count

string = input("Enter string: ")
result = vowels(string)

print("Total vowels =", result)
"""


# Q4. Armstrong Number Using Function
# Write a Python function that accepts a number and checks whether it is an Armstrong Number or
# not.
# Sample Input
# Enter number: 153
# Sample Output
# 153 is an Armstrong Number

"""def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        return True
    else:
        return False


num = int(input("Enter number: "))

if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")"""

# Q5. Sum of Digits Using Function
# Write a function that accepts a number and returns the sum of its digits.
# Sample Input
# Enter number: 12345
# Sample Output
# Sum of digits = 15
"""
def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


num = int(input("Enter number: "))
result = sum_of_digits(num)

print("Sum of digits =", result)"""





