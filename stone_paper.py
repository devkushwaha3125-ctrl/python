import random

cscore = 0
hscore = 0

while True:
    print(f"current scores you - {hscore} computer - {cscore}\n")
    user = int(input("1 fo rstone, 2 for paper , 3 for scissors choose :-"))

    com =random.randint(1,3)

    if user == 1 and com == 3:
        hscore+=1
        print("you won the round\n")

    elif user ==2 and com ==1:
        hscore+=1
        print("you won the round\n")

    elif user == 3 and com == 2:
        hscore+=1
        print("you won the round\n")

    elif user == com:
        print("it was draw ")

    else:
        cscore+=1
        print("computer won the round") 


    if cscore ==5:
        print("computer won this game 😈")
        break
    elif hscore == 5:
        print("congratulation you won 🥇") 
        break