# Code by Krypto Kiddo
# Subject: TC04 - Game Theory
# Aim : To make a Prisoner’s Dilemma generator that can detect whether a given payoff matrix makes the game a perfect, ambiguous or a wrong case of Prisoner’s Dilemma game. 

# Reference: https://plato.stanford.edu/entries/prisoner-dilemma/

print("Welcome to Prisoner's Dillema generator\n")
print("Do note that the payoff matrix will be generated in the following format:\n\n")
# Displaying the format of Payoff Matrix.
# This helps to limit the output to a symmetric PD game.
# I am too lazy to build an assymetric PD functionality.
print("_________________")
print("    |  C  |  D  |")
print("____⅃_____⅃_____⅃")
print("  C | R,R | S,T |")
print("____⅃_____⅃_____⅃")
print("  D | T,S | P,P |")
print("____⅃_____⅃_____⅃\n\n")

# Taking R,P,T,S from the user as input
R = input("What is the years of jail the players get if both deny/cooperate ?\n>> R = ") # Reward
P = input("And what is the years of jail both the players get if they both defect/confess ?\n>> P = ") # Punishment
T = input("How many years of jail will a player get if he is the only confessor/defecter ?\n>> T = ") # Temptation
S = input("And how many years of jail will a player get if he is the only denier/cooperator ?\n>> S = ") # Sucker


payoffMatrix = [[R,R],[S,T],[T,S],[P,P]] # This is our main matrix we need

# Making strings for representation purposes
x1 = str(R)+","+str(R)
x2 = str(S)+","+str(T)
x3 = str(T)+","+str(S)
x4 = str(P)+","+str(P)

# Displaying the final Payoff matrix received from the user
# The nature of the game will be decided based on this input
print("This is the received payoff matrix:\n\n")
print("____________________")
print(" p1,p2 |  C  |  D  |")
print("_______⅃_____⅃_____⅃")
print("     C |",x1,"|",x2,"|")
print("_______⅃_____⅃_____⅃")
print("     D |",x3,"|",x4,"|")
print("_______⅃_____⅃_____⅃\n\n")

# Here begins the logic to decide the nature of the game
if (T>R) and (R>P) and (P>S): print("Woah, it looks like this game is a PERFECT CASE of Prisoner's Dillema :)") # Perfect Case is where T>R>P>S
elif (T>R) and (R>P) and (P>=S): print("Woah, it looks like this game is a AMBIGUOUS CASE of Prisoner's Dillema :O") # In Ambiguous case T>R>P>=S
elif (T>=R) and (R>P) and (P>S): print("Woah, it looks like this game is a AMBIGUOUS CASE of Prisoner's Dillema :O") # Another Ambiguous case is where T>=R>P>S
else: print("Uh oh, it looks like this game is a WRONG CASE of Prisoner's Dillema :(")
