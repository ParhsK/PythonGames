import random
#picks a random word from a txt file
def pickRandWord():
        with open("wordsFile.txt") as word_file:
            words = word_file.read().split()
            random_word = random.choice(words)
            while len(random_word) < 5:
                random_word = random.choice(words)
            print(random_word) #prepei na einai >= 5 se grammata!
            return random_word

#prints the current state of Kremala and the incorrect letters
#def printCurrentState()

def initializeKremala(word
    leksh = []
    kremala = []
    incorrectLetters = []
    leksh.append([word])
    for i in len(word):
        kremala.append([_])
    return leksh, kremala, incorrectLetters

def askLetter(incorrectLetters):
    newLetter = input("Give a letter: ")[0] #diavazei ton prwto xarakthra apo ena string
    try:
        if newLetter.isalpha() == False:
            raise Exception()
        for i in incorrectLetters:
            if newLetter == incorrectLetters[i]:
                raise Exception()
    except:
        print("Wrong input. Please give a letter:")
        return askLetter(incorrectLetters)


#def kremalaHandler():

# given the game status decides if the word is found or the player lost
def checkGameStatus(kremala, leksh, incorrectLetters):
    if incorrectLetters > 5:
        print("6 incorrect letters. You lost. Try a new game!")
        return False
    else:
        if kremala == leksh:
            print("Congratulations! You have found the word!")
            return True


#asks for another game when the game ends
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

def main():
    #startGame = True
    #while startGame == True:
        word = pickRandWord()
        leksh, kremala, incorrectLetters = initializeKremala(word)
        #print(leksh, kremala) #printCurrentState()
        #while gameStatus == 0:
            #askLetter()
            #kremalaHandler()
            #gameStatus = checkGameStatus()
            #printCurrentState()
        #startGame = askForAnotherGame()
        return

main()