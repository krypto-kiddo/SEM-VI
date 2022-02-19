# Code by Krypto Kiddo
# Subject: GT - Game Theory
# Lab Assignment 3: Pure Strategy Nash Equilibrium

# CODE BEGINS BELOW

import random
import time
import pprint




def payOffMatrix(matrix, scr1, scr2):

    matrix.append(f'({scr1}, {scr2})')
    return matrix


def game():
    matrix = []
    total_turns = 5
    P1Score = 0
    P2Score = 0
    print("\t\t\tDemonstrating Pure Strategy Nash Equilibrium")
    print("Player 1 and Player 2 play simultaneously for 5 rounds")
    print("\n")
    for i in range(total_turns):

        currentP1scr = humansTurn()
        currentP2scr = playerTwo()
        matrix = payOffMatrix(matrix, currentP1scr, currentP2scr)
        P1Score += currentP1scr
        P2Score += currentP2scr

        print(f'Player 1 choses {currentP1scr}')
        print(f'Player 2 chosses {currentP2scr}')

        if currentP1scr == currentP2scr == 0:
            print(".........")
            time.sleep(1)
            print("Yaayyyyyiiiii it's a Pure Strategy Nash Equilibrium ")

        elif currentP1scr > currentP2scr:
            # one with larger number gives 2 points to one with small number and the smaller one gets smaller of the two numbers in points
            P1Score -= 2
            P2Score += 2
            P2Score += currentP2scr

        elif currentP1scr < currentP2scr:
            P1Score += 2
            P2Score -= 2
            P1Score += currentP1scr
        else:
            print("Hmmm.....the choices are equal but not equal to 0. You got a chance to maximize your score. Go get it!!")

            currentP1scr -= 1
            P1Score += 2
            P2Score -= 2
            P1Score += currentP1scr


        print("PayOff Matrix")
        pprint.pprint(matrix)

        print("Final scores")
        print(f'Player 1: {P1Score}')
        print(f'Player 2: {P2Score}')
        print("\n")


def humansTurn():
    randomInt = int(input("Choose any integer between 0 to 3 inclusive: "))
    return randomInt


def playerTwo():
    randomInt = random.randint(0, 3)
    return randomInt


game()

# END OF CODE

# HUGE THANKS TO @nitrogen404
