import random

def game(a):
    print("~~~~~~~~~~~~~~")
    print("Lets play ")
    print(" ")
    player=input("Choose rock paper or scissors ")

    print(" ")
    ## Cpu chooses at random
    cpu= random.randint(1,3)
    if cpu==1:
        print("Computer's Choice is Rock")
        c=1
    elif cpu==2:
        print("Computer's choice is Paper")
        c=2
    elif cpu==3:
        print("Computer's choice is Scissors")
        c=3

    print(" ")
    ##players choice
    print("player's choice is "+player+".")

    print (" ")
    ## giving the choice a number for results
    if player.lower()=="rock":
        p=1
    elif player.lower()=="paper":
        p=2
    elif player.lower()=="scissors":
        p=3
    else:
        print("Pick A Valid Choice")
        print("~~~~~~~~~~~~~~")
        return("none")


    ##results
    if p==1 and c==1:
        r= "Tie"
    elif p==1 and c==2:
        r= "Cpu Wins"
    elif p==1 and c==3:
        r= "Player Wins"
    elif p==2 and c==1:
        r= "Player Wins"
    elif p==2 and c==2:
        r= "Tie"
    elif p==2 and c==3:
        r= "Cpu Wins"
    elif p==3 and c==1:
        r= "Cpu wins"
    elif p==3 and c==2:
        r= "Player Wins"
    elif p==3 and c==3:
        r= "Tie"
    print("Results: " + r)
    print(" ")
    print("~~~~~~~~~~~~~~")
##this will loop the game
while True:
    game(0)


