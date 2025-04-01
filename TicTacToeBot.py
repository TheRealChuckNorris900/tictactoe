import math
a = [[" "]*5 for i in range(3)]
player = "O"
computer = "X"

def main():
   

    print("You are O")
    coords = 0
    while (not checkWin()):
        computerMove()
        playerMoves()

    
def spaceIsFree(x, y):
    if a[x][y] == " ":
        return True
    return False





def drawboard(a):
    for i in range(3):
    
        print(a[i][0] + "|" + a[i][1] + "|" + a[i][2])
        if i != 2:
            print("-+-+-")
    print("\n")
    

#double checks vallidity of input and gamw state
def insertLetter(letter, x, y):
    if spaceIsFree(x, y):
        a[x][y] = letter
        drawboard(a)
        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == "X":
                print("Bot wins")
                exit()
            else:
                print("Player Wins!")
                exit()
        return
    else:
        print("Invlaid position")
        coords = input("Please enter a new position: ")
        x = int(coords[0])
        y = int(coords[1])
        insertLetter(letter, x, y)
        return
    
def checkDraw():
    for i in range(3):
        for j in range(3):
            if a[i][j] == " ":
                return False
    return True

#logic
def checkWin():
    if (a[0][0] == a[0][1] and a[0][0] == a[0][2] and a[0][0] != ' '):
        return True
    elif (a[1][0] == a[1][1] and a[1][0] == a[1][2] and a[1][0] != ' '):
        return True
    elif (a[2][0] == a[2][1] and a[2][0] == a[2][2] and a[2][0] != ' '):
        return True
    elif (a[0][0] == a[1][0] and a[0][0] == a[2][0] and a[0][0] != ' '):
        return True
    elif (a[0][1] == a[1][1] and a[0][1] == a[2][1] and a[0][1] != ' '):
        return True
    elif (a[0][2] == a[1][2] and a[0][2] == a[2][2] and a[0][2] != ' '):
        return True
    elif (a[0][0] == a[1][1] and a[0][0] == a[2][2] and a[0][0] != ' '):
        return True
    elif (a[2][0] == a[1][1] and a[2][0] == a[0][2] and a[2][0] != ' '):
        return True
    else:
        return False
    
#logic copied and pasted, check who wins in each scenario
def checkWhichMarkWon(mark):
    if (a[0][0] == a[0][1] and a[0][0] == a[0][2] and a[0][0] == mark):
        return True
    elif (a[1][0] == a[1][1] and a[1][0] == a[1][2] and a[1][0] == mark):
        return True
    elif (a[2][0] == a[2][1] and a[2][0] == a[2][2] and a[2][0] == mark):
        return True
    elif (a[0][0] == a[1][0] and a[0][0] == a[2][0] and a[0][0] == mark):
        return True
    elif (a[0][1] == a[1][1] and a[0][1] == a[2][1] and a[0][1] == mark):
        return True
    elif (a[0][2] == a[1][2] and a[0][2] == a[2][2] and a[0][2] == mark):
        return True
    elif (a[0][0] == a[1][1] and a[0][0] == a[2][2] and a[0][0] == mark):
        return True
    elif (a[2][0] == a[1][1] and a[2][0] == a[0][2] and a[2][0] == mark):
        return True
    else:
        return False

#ask user for input
def playerMoves():
    coords = (input("Put in the coords for your move: "))
    x = int(coords[0])
    y = int(coords[1])
    insertLetter(player, x, y)
    return

#logic behin choosing which move is the best
def computerMove():#With MinMax function
    best_Score = -800#small number
    bestMove_X = 0#doesnt matter, needs to be initialised. We go through nodes, and we have one for each combination
    bestMove_Y = 0

    for i in range(3):
        for j in range(3):
            if a[i][j] == " ":
                a[i][j] = computer
                score = minimax(a, False)
                a[i][j] = " "
                if score > best_Score:
                    best_Score = score
                    bestMove_X = i
                    bestMove_Y = j
    insertLetter(computer, bestMove_X, bestMove_Y)
    return

#logic of minmax: recursive function the checks each possibility in this case, and recursively works from the back to the first move
#maximises when its your turn, minimizes when it is not your turn

def minimax(a, isMaximizing):
    #at end of recursion, check outcome
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0
    
    if isMaximizing:
        best_Score = -800
        for i in range(3):
            for j in range(3):
                if a[i][j] == " ":
                    a[i][j] = computer
                    score = minimax(a, False)
                    a[i][j] = " "
                    if score > best_Score:
                        best_Score = score
        
        return best_Score
    else:
        best_Score = 800
        for i in range(3):
            for j in range(3):
                if a[i][j] == " ":
                    a[i][j] = player
                    score = minimax(a, True)
                    a[i][j] = " "
                    if score < best_Score:
                        best_Score = score
        
        return best_Score


if __name__ == '__main__':
    main()