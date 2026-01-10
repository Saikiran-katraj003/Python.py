import random

'''
1 for snake
0 for gun
-1 for water
 '''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
YouDict = {"snake": 1, "gun": 0, "water": -1}
reverseDict= {1: "snake", 0: "gun", -1: "water"}

you = YouDict[youstr] 
          
          #by now we have 2 variables computer and you.

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):  
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): #if computer and you chose same choice then it's a draw
        print("You win!")

    elif(computer ==-1 and you == 0): #if computer chose -1 and you chose 0 then you lose 
        print("You Lose!")

    elif(computer == 1 and you == -1): #if computer chose 1 and you chose -1 then you lose 
        print("You lose!")

    elif(computer ==1 and you == 0): #if computer chose 1 and you chose 0 then you Win
        print("You Win!")

    elif(computer ==0 and you == -1): #if computer chose 0 and you chose -1 then you Win 
        print("You Win!")

    elif(computer == 0 and you == 1): #if computer chose 0 and you chose 1 then you lose 
        print("You Lose!")

    else:
        print("Something went wrong!") #if anything wrong in ifelse ladder then it will print Something went wrong




