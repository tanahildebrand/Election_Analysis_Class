#Incorporate the random library
import random

#Print Title
print("Let's Play Rock, Paper, Scissors!")

#User Selection
choice = input("What's your selection? Choose rock(R), paper(P), scissors(S)")
choice = choice.lower()

list = ["R", "P", "S"]
computer = random.choice(list)

# Determine the grade.
if choice == computer:
    print('You tied!')
elif choice == "R" and computer == "P":
    print('Computer Wins!')
elif choice == "P" and computer == "S":
    print('Computer Wins!')
elif choice == "S" and computer == "R":
    print('Computer Wins!')
else:
    print('You win!')