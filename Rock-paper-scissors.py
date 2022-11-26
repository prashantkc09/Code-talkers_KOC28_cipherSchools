import random
print("Welcome to Rock paper and scissors game. Game will be out of 5")
list=["rock","paper","scissors"]
name=input("Player's names:")
comp=0
play=0
while play<5 and comp<5:
    a=input("rock,paper,scissors?")
    if a=="end the game":
            break
    elif a not in list:
        print("Choose from rock, paper and scissors only.")
    else:
        b=random.choice(list)
        if b==a:
            print("Comp:",b)
            print("It's A Tie")
        elif a=='rock' and b=='scissors':
            print("Comp:",b)
            print("Winner:-",name,",Rock smashes scissors")
            play=play+1
            print('Player:',play,'Comp:',comp)
        elif a=='rock' and b=='paper':
            print("Comp:",b)
            print("Winner: Comp ,Paper covers rock ")
            comp=comp+1
            print('Player:',play,'Comp:',comp)
        elif a=='paper' and b=='scissors':
            print("Comp:",b)
            print("Winner: Comp ,Scissors cuts paper")
            comp=comp+1
            print('Player:',play,'Comp:',comp)
        elif a=='paper' and b=='rock':
            print("Comp:",b)
            print("Winner:",name,"Paper covers rock")
            play=play+1
            print('Player:',play,'Comp:',comp)
        elif a=='scissors' and b=='paper':
            print("Comp:",b)
            print("Winner:",name,",Scissors cuts paper")
            play=play+1
            print('Player:',play,'Comp:',comp)
        elif a=='scissors' and b=='rock':
            print("Comp:",b)
            print("Winner: Comp , Rock smashes scissors")
            comp=comp+1
            print('Player:',play,'Comp:',comp)
print("!!Game over!!")
if comp==5:
    print("You lost,Comp wins")
    print("Final Scores:\n Cpu:",comp,"\nUser:",play)
elif play==5:
    print("Congratulations",name,'You Won')
    print("Final Scores:\n Cpu:",comp,"\nUser:",play)
else:
    print("Final Scores:\n Cpu:",comp,"\nUser:",play)