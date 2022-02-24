# Code by Krypto Kiddo
# Subject: TC04 - Game Theory | Lab Assignment 04
# Aim : To calculate Maximin, Minimax, Saddle Point and MSNE in a given game.  

# Reference: https://youtu.be/Hw2XkWIv7Ww
# Russia-Ukraine war kinda began today with a heated up military operation in Ukraine. God bless them

# CODE BEGINS BELOW
import numpy as np

gameMatrix = np.array([[-3,6],[-2,4],[2,3]])

print("Given game matrix is:\n")
for row in gameMatrix:
    print(row)


colMax = gameMatrix.max(axis=0)
listOfMins =  gameMatrix.min(axis=1)

colMax.sort()
listOfMins.sort()


maximin = listOfMins[-1]
minimax = colMax[0]

print("\nMaximin Value is : ",maximin)
print("Minimax Value is : ",minimax)

if(minimax == maximin):
    print("\nVOILA! Maximin and Minimax values have MATCHING VALUES")
    print("Thus, Game Value is : ",maximin)
    print("\nSearching for Saddle Point value...")
    saddleCol = list(gameMatrix.max(axis=0)).index(maximin)
    saddleRow = list(gameMatrix.min(axis=1)).index(minimax)
    print("Found Saddle coordinates")
    print("\nSaddle point found at column number : ",saddleCol+1)
    print("And at the row number :",saddleRow+1)
    print("\n\nHence, MSNE exists at ",saddleRow+1,",",saddleCol+1," in the given matrix")
else:
    print("Oops, it looks like the Saddle point wasn't found since your Maximin and Minimax values donot converge!")

# END OF CODE
