#! python3
#A Game of Tic Tac Toe
#Still need to simplify code
import sys 

b = ["   " for _ in range(9)]

def printBox():
    print(f"{b[0]}|{b[1]}|{b[2]}   =>   1,2,3")
    print("---+---+---")
    print(f"{b[3]}|{b[4]}|{b[5]}   =>   4,5,6")
    print("---+---+---")
    print(f"{b[6]}|{b[7]}|{b[8]}   =>   7,8,9")

def checkNotBlank(i):
    if b[i] != "   ":
        print("Space already taken")
        return True
    
# def playAgain():
#     while True:
#         try:
#             again = input("Would you like to play again? (Y/N): ").upper()
#         except:
#             print("invalid input")
#         if again == "Y":
#             p1list=[] 
#             p2list=[]
#             b = ['   ' for _ in range(9)]
#             print("\nNEW GAME!")
#             printBox() #prints fresh box
#             break
#         elif again == "N":
#             print("Thanks for playing!\nExiting program...")
#             sys.exit()
#         else: 
#             print("invalid input")
#             continue
    
wins = [
[0,1,2],
[3,4,5],
[6,7,8],
[0,4,8],#diag
[2,4,6],
[0,3,6],#vert
[1,4,7],
[2,5,8],
]

#empty lists that will hold the player's inputs as the game goes on
p1list=[] 
p2list=[]

print("\nWELCOME TO TIC TAC TOE 3.0!!!")
printBox() #prints initial box
#The Game Begins...
while True:
    #Player 1 Turn
    while True:
        try:
            p1inp= int(input("Player 1, enter your move: "))-1
            if not (8 >= p1inp >= 0):
                print("Input must be between 1 and 9")
                continue
            elif checkNotBlank(p1inp):
                continue
            break
        except ValueError:
            print("\nINVALID INPUT, TRY AGAIN…")
            continue
    b[p1inp]=" X "
    print("\n")
    printBox()
    print()
    p1list.append( int(p1inp) ) # holds a list of all P1 input
    setp1 = set(p1list) # converts P1 input list into a set
    for win in wins:
        setwin = set(win)
        setp1 = set(p1list)
        print(setwin, setp1)
        won = setwin.issubset(setp1)
        tie = "   " not in b
    # p1Same = p1Set & setWins # finds the elements that are the same between wins and P1 set and puts it into a set
    # if p1Same in setWins:
        if won:
            print("\nP1 wins!")
            while True:
                try:
                    again = input("Would you like to play again? (Y/N): ").upper()
                except:
                    print("invalid input")
                if again == "Y":
                    p1list=[] 
                    p2list=[]
                    b = ['   ' for _ in range(9)]
                    print("\nNEW GAME!")
                    printBox() #prints fresh box
                    break
                elif again == "N":
                    print("Thanks for playing!\nExiting program...")
                    sys.exit()
                else: 
                    print("invalid input")
                    continue
        elif tie:
            print("\nTIE!")
            playAgain()
    #Player 2 Turn
    while True:
        try:
            p2inp= int(input("Player 2, enter your move: "))-1
            if not (8 >= p2inp >= 0):
                print("Input must be between 1 and 9")
                continue
            elif checkNotBlank(p2inp):
                continue
            break
        except ValueError:
            print("\nINVALID INPUT, TRY AGAIN…")
            continue
    b[p2inp]=" O "
    print("\n")
    printBox()
    print()
    p2list.append( int(p2inp) ) # holds a list of all P1 input
    setp2 = set(p2list) # converts P1 input list into a set
    for win in wins:
        setwin = set(win)
        setp2 = set(p2list)
        print(setwin, setp2)
        won = setwin.issubset(setp2)
        tie = "   " not in b
        if won:
            print("\nP2 wins!")
            while True:
                try:
                    again = input("Would you like to play again? (Y/N): ").upper()
                except:
                    print("invalid input")
                if again == "Y":
                    p1list=[] 
                    p2list=[]
                    b = ['   ' for _ in range(9)]
                    print("\nNEW GAME!")
                    printBox() #prints fresh box
                    break
                elif again == "N":
                    print("Thanks for playing!\nExiting program...")
                    sys.exit()
                else: 
                    print("invalid input")
                    continue
        elif tie:
            print("\nTIE!")
            playAgain()