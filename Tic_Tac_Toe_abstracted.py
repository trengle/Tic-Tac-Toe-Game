#! python3
#A Game of Tic Tac Toe
#Still need to bugs where it doesn't detect duplicate wins
import sys 

def printBox(b):
    print(f"{b[0]}|{b[1]}|{b[2]}   =>   1,2,3")
    print("---+---+---")
    print(f"{b[3]}|{b[4]}|{b[5]}   =>   4,5,6")
    print("---+---+---")
    print(f"{b[6]}|{b[7]}|{b[8]}   =>   7,8,9")

def checkNotBlank(b, i):
    if b[i] != "   ":
        print("Space already taken")
        return True
    
def playAgain():
    while True:
        try:
            again = input("Would you like to play again? (Y/N): ").upper()
        except:
            print("invalid input")
        if again == "Y":
            print("\nNEW GAME!")
            return True
        elif again == "N":
            print("Thanks for playing!\nExiting program...")
            return False
        else: 
            print("invalid input")
            continue

def tic_tac_toe():
    b = ["   " for _ in range(9)] #initializes the empty list of symbols
    #list of all possible win combos in the form of sets
    winset = [
    {0,1,2},
    {3,4,5},
    {6,7,8},
    {0,4,8},#diag
    {2,4,6},
    {0,3,6},#vert
    {1,4,7},
    {2,5,8},
    ]
    inplist=[[],[]] #empty lists that will hold the player's inputs as the game goes on
    print("\nWELCOME TO TIC TAC TOE 3.0!!!")
    printBox(b) #prints initial box
    turn = 0
    #The Game Begins...
    while True:
        #New Turn
        won = False
        tie = False
        current_player = (turn%2)
        symbols = [" X ", " O "]
        while True:
            try:
                pinp= int(input(f"Player {current_player+1}, enter your move: "))-1
                if not (8 >= pinp >= 0):
                    print("Input must be between 1 and 9")
                    continue
                elif checkNotBlank(b,pinp): #checks if the space is already taken
                    continue
                break
            except ValueError:
                print("\nINVALID INPUT, TRY AGAIN…")
                continue
        b[pinp] = symbols[current_player] #adds the current symbol to the board
        print("\n")
        printBox(b)
        print()
        inplist[current_player].append( int(pinp) ) # holds a list of all player input
        setlist=[set(inplist[0]),set(inplist[1])] #list containing the 2 sets based off the 2 input lists
        # for win in winset:
        #     print(win)
        # print(setlist[current_player])
        for win in winset:
            print(f"win is {win} and current input set is {setlist[current_player]}") #diagnostic
            if win.issubset(setlist[current_player]): #THIS IS THE BUGGY LINE OF CODE
                won=True
        if won:
            print(f"\nP{current_player+1} wins!")
            if playAgain():
                b = ['   ' for _ in range(9)]
                printBox(b) #prints fresh box
                inplist=[[],[]] #resets input lists to being empty
                break
            else: sys.exit()
        tie = "   " not in b
        if tie:
            print("\nTIE!")
            if playAgain():
                b = ['   ' for _ in range(9)]
                printBox(b) #prints fresh box
                inplist=[[],[]] #resets input lists to being empty
                break
            else: sys.exit()
        turn+=1

if __name__ == "__main__":
    tic_tac_toe()