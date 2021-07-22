import random
def hangman():
    word=random.choice(["wonderwomen","thor","ironman","avengers","india","kalam","savage","phone","sacraments","bright","clock","dice","aesthetic"])
    validletter="abcdefghijklmnopqrstuvwxyz"
    turns=10
    guessmade=""
    while(len(word)>0):
        again=0
        main=""
        for letter in word:
            if letter in guessmade:
                main+=letter
            else:
                main+="_"+" "


        print("guess the letter of word",main)
        guess=input()

        if main==word:
            print("***********************   YOU WIN   ***************************")
            print("THANKS FOR SAVING THE KIND MAN")
            break

        if guess in validletter:
            if len(guessmade)>0:
             if guess not in guessmade:
                guessmade+=guess
             else:
                print("you guess the letter which was entered before\ntry different letter ")
                again=1
            else:
                guessmade+=guess

        else:
            print("plz enter valid letter")
            guess=input()
        if again==0:
         if guess not in word:
            turns-=1
            print(f"{turns} turns left")
            if turns==9:
                print("-------")
            if turns ==8:
                print("-------")
                print("   0   ")
            if turns ==7:
                print("-------")
                print("   0   ")
                print("   |   ")
            if turns ==6:
                print("-------")
                print("   0   ")
                print("   |   ")
                print("  /    ")
            if turns ==5:
                print("-------")
                print("   0   ")
                print("   |   ")
                print("  / \  ")
            if turns ==4:
                print("-------")
                print(" \ 0   ")
                print("   |   ")
                print("  / \  ")
            if turns ==3:
                print("-------")
                print("  \o/  ")
                print("   |   ")
                print("  / \  ")
            if turns ==2:
                print("-------")
                print("  \o|/ ")
                print("   |   ")
                print("  / \  ")
            if turns ==1:
                print("-------")
                print("  \o_|/  ")
                print("   |   ")
                print("  / \  ")
            if turns ==0:
                print("You let the kind man die")
                print("**************************   YOU LOSE    **********************************")
                print("-------")
                print("   0_|  ")
                print("  /|\  ")
                print("  / \  ")
                break


name=input("enter ur name: ")
print("WELCOME "+name.upper())
print("try to Guess the word in 10 attempts")
ch='y'
while(ch=="y" or ch=="Y"):
 hangman()
 ch=input("want to play again enter(y for yes or anything except y for no)")

