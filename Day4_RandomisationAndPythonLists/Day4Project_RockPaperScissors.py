import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, and 3 for exit.\n")
while choice != "3":
    if choice == "0":
        print(rock)
    elif choice == "1":
        print(paper)
    elif choice == "2":
        print(scissors)
    elif choice == "3":
        break
    else:
        print("Invalid choice! You lose!")
        break
    computer = ["Rock", "Paper", "Scissors"]
    compChoice = random.choice(computer)
    print("Computer choose:")
    if compChoice == "Rock" and choice == "0":
        print(rock)
        print("Draw!")
    elif compChoice =="Rock" and choice == "1":
        print(rock)
        print("You win!")
    elif compChoice =="Rock" and choice == "2":
        print(rock)
        print("You lose!")
    elif compChoice == "Paper" and choice == "0":
        print(paper)
        print("You lose!")
    elif compChoice == "Paper" and choice == "1":
        print(paper)
        print("Draw!")
    elif compChoice == "Paper" and choice == "2":
        print(paper)
        print("You win!")
    elif compChoice == "Scissors" and choice == "0":
        print(scissors)
        print("You win!")
    elif compChoice == "Scissors" and choice == "1":
        print(scissors)
        print("You lose!")
    else:
        print(scissors)
        print("Draw!")