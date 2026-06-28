"""import random 

number = random.randint(1,100)
count= 0
while True: #infinite loop
  count += 1
  user =  int(input("enter the number "))

  if user == number:
    print("you won man ")
    print(f"you took {count} to win") 
    break
  
  elif user < number:
    print(f"too low, your value is {user} and computers value {number}")

  elif user >number:
    print("too high vlue guess lower value") """


#user have only five chances and those chances are over either he will win or lose
"""import random

number = random.randint(1, 100)
count = 0
max_chances = 5

while count < max_chances:
    count += 1
    user = int(input("Enter the number: "))

    if user == number:
        print("You won!")
        print(f"You took {count} chances to win.")
        break

    elif user < number:
        print("Too low! Guess a higher number.")

    else:
        print("Too high! Guess a lower number.")

    print(f"Chances left: {max_chances - count}")

if count == max_chances and user != number:
    print("You lost!")
    print(f"The correct number was {number}")"""



# streamlit  
#