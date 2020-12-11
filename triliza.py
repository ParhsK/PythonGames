def initializeTriliza():
    triliza = []
    triliza.append([0, 0, 0])
    triliza.append([0, 0, 0])
    triliza.append([0, 0, 0])
    return triliza

# Prints message and asks who the first player is
def askFirstPlayer():
    firstPlayer = input("Which Player is first? ")
    try:
        intFirstPlayer = int(firstPlayer)
        if intFirstPlayer != 1 and intFirstPlayer != 2:
            print("Player must be 1 or 2")
            raise Exception()
        else:
            return intFirstPlayer
    except:
        print("Wrong input.")
        return askFirstPlayer()

# Checks if the current move is acceptable in this game
def checkMove(row, column, currentPlayer, triliza):
    if triliza[row][column] != 0:
        print("Wrong move. Cell already filled.")
        return False
    return True

# Prints message and asks for move by current player
def askMove(currentPlayer, triliza):
    newMove = input("Give move for player " + str(currentPlayer) + ": ")
    try:
        row, column = map(int, newMove.split())
        row = row - 1
        column = column - 1
        if column < 0 or row < 0 or column > 2 or row > 2:
            raise Exception()
        if checkMove(row, column, currentPlayer, triliza) == False:
            return askMove(currentPlayer, triliza)
        return row, column
    except:
        print("Wrong input, try again.")
        return askMove(currentPlayer, triliza)

# given the game status prints a human readable triliza
def printTriliza(triliza):
    for row in triliza:
        print(" ------------- ")
        for cell in row:
            cellPrinted = ' '
            if cell == 1:
                cellPrinted = 'X'
            elif cell == 2:
                cellPrinted = 'O'
            print(" | " + cellPrinted, end = '')
        print(" | ")
    print(" ------------- ")
    return


def askForAnotherGame():
    answer = input("Do you want to play another round? Y/y or N/n ")
    startGame = True
    if (answer == "Y") or (answer == "y"):
        startGame = True
    elif (answer == "N") or (answer == "n"):
        startGame = False
    else:
        print("Wrong input. Try again! ")
        return askForAnotherGame()
    return startGame

def trilizaHandler(triliza, row, column, currentPlayer):
    triliza[row][column] = currentPlayer
    return triliza

# given the game state decides if its a draw, win or still playable
def checkGameStatus(triliza):
    result = checkRows(triliza)
    if result != 0:
        return result
    result = checkColumns(triliza)
    if result != 0:
        return result
    result = checkDiagonals(triliza)
    return result

def checkRows(triliza):
    for row in triliza:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkColumns(triliza):
    columns = [[triliza[i][j] for i in range(3)] for j in range(3)]
    for row in columns:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(triliza):
    if len(set([triliza[i][i] for i in range(len(triliza))])) == 1:
        return triliza[0][0]
    if len(set([triliza[i][len(triliza)-i-1] for i in range(len(triliza))])) == 1:
        return triliza[0][len(triliza)-1]
    return 0

def main():
    startGame = True
    while startGame == True:
        triliza = initializeTriliza()
        player = askFirstPlayer()
        gameStatus = 0
        while gameStatus == 0:
            if 0 not in [triliza[i][j] for i in range(3) for j in range(3)]:
                gameStatus = -1
                break
            rowMove, columnMove = askMove(player, triliza)
            triliza = trilizaHandler(triliza, rowMove, columnMove, player)
            printTriliza(triliza)
            gameStatus = checkGameStatus(triliza)
            player = (player % 2) + 1
        if gameStatus > 0:
            print("Player " + str((player % 2) + 1) + " wins!")
        else:
            print("It's a draw!")
        startGame = askForAnotherGame()
    return

main()