import random

def game():
    print("~~~~~~~~~~~~~~")
    print("Lets play ")
    print(" ")
    player=input("Choose rock paper or sissors ")

    print(" ")
    ## Cpu chooses at random
    cpu= random.randint(1,3)
    if cpu==1:
        print("Computer's Choice is Rock")
        c=1
    elif cpu==2:
        print("Computer's choice is paper")
        c=2
    elif cpu==3:
        print("Computer's choice is Sissors")
        c=3

    print(" ")
    ##players choice
    print("player's choice is "+player+".")

    print (" ")
    ## giving the choice a number for results
    if player=="rock":
        p=1
    elif player=="Rock":
        p=1
    elif player==" Rock":
        p=1
    elif player==" rock":
        p=1
    elif player=="Paper":
        p=2
    elif player==" Paper":
        p=2
    elif player=="paper":
        p=2
    elif player==" paper":
        p=2
    elif player=="Sissors":
        p=3
    elif player==" Sissors":
        p=3
    elif player=="sissors":
        p=3
    elif player==" sissors":
        p=3

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
    game()

game()



