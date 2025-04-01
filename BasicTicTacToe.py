import math
a = [[" "]*5 for i in range(3)]
player = "O"
computer = "X"

def main():
   

    print("You are crosses")
    print("Input the coordinates where you want to put a cross")
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


def checkWin():
    if (a[0][0] == a[0][1] and a[0][0] == a[0][2] and a[0][0] != ' '):#top row
        return True
    elif (a[1][0] == a[1][1] and a[1][0] == a[1][2] and a[1][0] != ' '):#middle row
        return True
    elif (a[2][0] == a[2][1] and a[2][0] == a[2][2] and a[2][0] != ' '):#bottom row
        return True
    elif (a[0][0] == a[1][0] and a[0][0] == a[2][0] and a[0][0] != ' '):#left column
        return True
    elif (a[0][1] == a[1][1] and a[0][1] == a[2][1] and a[0][1] != ' '):#middle column
        return True
    elif (a[0][2] == a[1][2] and a[0][2] == a[2][2] and a[0][2] != ' '):#right column
        return True
    elif (a[0][0] == a[1][1] and a[0][0] == a[2][2] and a[0][0] != ' '):#diagonal 1
        return True
    elif (a[2][0] == a[1][1] and a[2][0] == a[0][2] and a[2][0] != ' '):#diagonal 2
        return True
    else:
        return False
    
def playerMoves():
    coords = (input("Put in the coords for your move: "))
    x = int(coords[0])
    y = int(coords[1])
    insertLetter(player, x, y)
    return

def computerMove():
    coords = (input("Put in the coords for computer move: "))
    x = int(coords[0])
    y = int(coords[1])
    insertLetter(computer, x, y)
    return

if __name__ == '__main__':
    main()