import random 

com=random.choice(['r','p','s'])
you=input("Enter your choice:")

print(f"Computer choce {com} and you chose {you}.")
if you not in ['r', 'p', 's']:
    print("Wrong input")
else:
    if com == you:
        print("Draw")
    elif(com == 'r'and you=='s') or (com == 'p'and you=='r') or (com == 's' and you=='p'):
        print("You lose!")
    else:
        print("You win!")
