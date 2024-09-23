import random

item = ["Rock", "Paper", "Scissors"]

while True:
    process = random.choice(item)

    player = None
    while player not in item:
        player = input("Choose one: Rock, Paper, or Scissors: ").capitalize()

    print("Player Choice: " + player)
    print("Computer Choice: " + process)

    if player == process:
        print("It's a tie :/")
    elif player == "Rock":
        if process == "Paper":
            print("Computer wins! :D")
        else:
            print("You win! :D")
    elif player == "Paper":
        if process == "Scissors":
            print("Computer wins! :D")
        else:
            print("You win! :D")
    elif player == "Scissors":
        if process == "Rock":
            print("Computer wins! :D")
        else:
            print("You win! :D")

    pagain = input("Play again? (yes/no): ").lower()
    if pagain != "yes":
        break
print("Bye buddy Thanks for playing :)")