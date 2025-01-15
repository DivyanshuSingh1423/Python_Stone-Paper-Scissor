import random
'''
1 for rock
-1 for paper
0 for scissor
'''


computer = random.choice([-1, 1, 0])
youstr=input("Enter your choice :")
youDict={"r" : 1,"p" : -1,"s":0}
reverseDict={1 : "Rock",-1 :"Paper",0:"Scrissor"}
you = youDict[youstr]

print(f"Computer -> {reverseDict[computer]} \nYou -> {reverseDict[you]}")

if (computer == you):
    print("Draw !!!")

else :
    if(computer == -1 and you == 1):
        print("You Won !!!")

    elif(computer == -1 and you == 0):
        print("You Lose !!!")

    elif(computer == 1 and you == -1):
        print("You Won !!!")

    elif(computer == 1 and you == 0):
        print("You LOse !!!")

    elif(computer == 0 and you == 1):
        print("You Won !!!")

    elif(computer == 0 and you == -1):
        print("You Lose !!!")

    else:
        print("sommething went wrong!!")

   

