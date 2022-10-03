import random

wlt = [0, 0, 0]

rig = -1 # -1 --> random; 0 --> always win; 1 --> always lose
av = ["Rock", "Paper", "Scissors"]

while True:
    playerinput = ""
    computerinput = ""
    while playerinput != "r" and playerinput != "p" and playerinput != "s":
        playerinput = input("Lets play rock paper scissors!\nType \"r\", \"p\", or \"s\" to play rock, paper, or scissors respectively.\n").lower()
    if playerinput == "r":
        playerinput = 0
    elif playerinput == "p":
        playerinput = 1
    elif playerinput == "s":
        playerinput = 2
    
    if rig == -1:
        computerinput = random.randint(0, 2)
    
    elif rig == 0:
        if playerinput == 0:
            computerinput = 2
        else:
            computerinput = playerinput - 1
    
    elif rig == 1:
        if playerinput == 2:
            computerinput = 0
        else:
            computerinput = playerinput + 1
    
    if playerinput == computerinput:
        print("Tie!")
        wlt[2] += 1
    
    else:
        if playerinput - 1 == computerinput:
            print("You win!")
            wlt[0] += 1
        elif playerinput + 1 == computerinput:
            print("You lose!")
            wlt[1] += 1
        elif playerinput == 2 and computerinput == 0:
            print("You lose!")
            wlt[1] += 1
        elif playerinput == 0 and computerinput == 2:
            print("You win!")
            wlt[0] += 1
    
    for i in range(3):
        if playerinput == i:
            print("Player did " + av[i])
    for i in range(3):
        if computerinput == i:
            print("Computer did " + av[i])
    print("\nWins: " + str(wlt[0]) + "\nLosses: " + str(wlt[1]) + "\nTies: " + str(wlt[2]) + "\n")
