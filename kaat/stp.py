import random


user_input=input("Enter a choice : (rock , paper , scissors)")
possible_actions=["rock","paper","scissors"]
computer_actions=random.choice(possible_actions)
print(computer_actions)
if user_input==computer_actions:
    print("Tie")
elif ((user_input=="rock") and (computer_actions=="paper")) or ((user_input=="scissors") and (computer_actions=="rock")) or ((user_input=="paper") and (computer_actions=="scissors")):
    print("LOL")
else:
    print("K/O")