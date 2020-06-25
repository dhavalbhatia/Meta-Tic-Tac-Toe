from UltimateMetaTTT import NumTicTacToe, ClassicTicTacToe, MetaTicTacToe

def getEntry(player, turn, entries):
    '''
    Prompts specified player for number to place on board; reprompts if that 
    number is not valid.
    Inputs:
       player (int) - number of current player (1 or 2)
       entries (list) - numbers already placed on board
    Returns: int to place on board
    '''
    
    if turn % 2 == 0:
        numDescription = 'even'
        lowerRange = 2
        upperRange = 8        
    else:
        numDescription = 'odd'
        lowerRange = 1
        upperRange = 9         
    prompt = 'Player {}, please enter an {} number ({}-{}): '
    prompt = prompt.format(player, numDescription, lowerRange, upperRange)
    entry = input(prompt)
    
    list = []
    for i in range(1,10):
        list.append(str(i))
    
    while entry not in list:
        print("Please enter a valid number")
        entry = input(prompt)
    

    correct = False
    while correct == False:
        if numDescription == "odd":
            if int(entry) % 2 == 0:
                print("Error: entry not odd . Player 1, please enter an odd number (1-9):")
                correct = False
                entry = int(input(prompt))
            else:
                correct = True
                
        elif numDescription == 'even':
            if int(entry) % 2 != 0:
                print("not even")
                entry = int(input(prompt))
                correct = False
            else:
                correct = True
                
    return int(entry)

def playAgain():
    '''
    Asks if a new game should be started. A valid answer is any entry that begins
    with y/Y/n/N.
    Inputs: none
    Returns: True if a new game should start; False otherwise
    '''
    playAgain=' ' 
    # validate user's input
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain=input("Do you want to play another game? (Y/N) ")
    return playAgain[0].upper() == "Y"   

def getCoord(player, dimension):
    '''
    Prompts for an index value corresponding to either the row or column (as
    described by dimension) of a square on the board
    Inputs:
       player (int) - number of current player (1 or 2)
       dimension (str) - describes what the index relates to (e.g. 'row' or 'column')
    Returns: int index (either row or column)
    '''
    #validate
    
    
    index =input('Player ' + str(player) + ', please enter a ' + dimension+': ')
    
    while index not in ['0', '1', '2']:
        print('Error', dimension, 'not in range ')
        index =input('Player ' + str(player) + ', please enter a ' + dimension+': ')
    return int(index)


def isGameOver(myBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (NumTicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    if myBoard.isWinner():
        myBoard.drawBoard()
        print ('Player', player ,"wins. Congrats!")           
        if player == 1:
            return 'X'
        elif player == 2:
            return 'O'
    elif myBoard.boardFull():
        myBoard.drawBoard()
        print ("It's a tie.")             
        return 'D'  
    return False
def isGameOverMain(MainBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (NumTicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    if MainBoard.isWinner():
        MainBoard.drawBoard()
        print ('Player', player ,"wins. Congrats!")           
        return True
    elif MainBoard.boardFull():
        MainBoard.drawBoard()
        print ("It's a tie.")             
        return True  
    return False

def playNumTTT(player):
    TITLE = "Starting new Numerical Tic Tac Toe game"
    print("-"*len(TITLE))
    print (TITLE)
    print("-"*len(TITLE))
    myBoard=NumTicTacToe()
    gameOver=False
    currentplayer = player
    turn = 0
    entries = []
    while not gameOver:
        myBoard.drawBoard()
        
        # get input from user
        entry = getEntry(currentplayer, turn+1, entries)
        row = getCoord(currentplayer, 'row')
        col = getCoord(currentplayer, 'column')
        
        # update board and check if game continues
        if myBoard.update(row, col, entry):
            entries.append(entry)
            gameOver = isGameOver(myBoard, currentplayer)
            if gameOver != False:
                return gameOver
            turn = (turn+1) % 2                
        # need to reprompt for new input for given player
            if currentplayer == 1:
                currentplayer = 2
            else:
                currentplayer = 1
        else:
            print("Error: could not make move!")

def playClassTTT(player):
    TITLE = "Starting new Classical Tic Tac Toe game"
    print("-"*len(TITLE))
    print (TITLE)
    print("-"*len(TITLE))
    myBoard=ClassicTicTacToe()
    gameOver=False
    currentplayer = player
    turn = 0
    entries = []
    while not gameOver:
        myBoard.drawBoard()        
        # get input from user
        row = getCoord(currentplayer, 'row')
        col = getCoord(currentplayer, 'column')
        if (turn+1) == 1:
            entry = "X"
        elif (turn+1) == 2:
            entry = "O"
        
        # update board and check if game continues
        if myBoard.update(row, col, entry):
            entries.append(entry)
            gameOver = isGameOver(myBoard, currentplayer)
            if gameOver != False:
                return gameOver
            turn = (turn+1) % 2                
        # need to reprompt for new input for given player
            if currentplayer == 1:
                currentplayer = 2
            else:
                currentplayer = 1
        else:
            print("Error: could not make move!")
    

def main():
    newGame=True
    while newGame:
        player = 1
        TITLE = "Starting new Numerical Tic Tac Toe game"
        print("-"*len(TITLE))
        print (TITLE)
        print("-"*len(TITLE))
        MainBoard = MetaTicTacToe('MetaTTTconfig.txt')
        gameOver=False
        turn = 0
        entries = []
        while not gameOver:
            MainBoard.drawBoard()
            # get input from user
            row = getCoord(turn+1, 'row')
            col = getCoord(turn+1, 'column')
            while not MainBoard.squareIsEmpty(row, col):
                print("error game has already been played at that tile")
                row = getCoord(turn+1, 'row')
                col = getCoord(turn+1, 'column')
            if MainBoard.board[row][col] == 'c':
                entry = playClassTTT(player)
            elif MainBoard.board[row][col] == 'n':
                entry = playNumTTT(player)
              
           # update board and check if game continues
            if MainBoard.update(row, col, entry):
               entries.append(entry)
               gameOver = isGameOver(MainBoard, turn+1)
               turn = (turn+1) % 2
               if player == 1:
                  player = 2
               else:
                  player = 1
        newGame = playAgain()         
    print('Thanks for playing! Goodbye.')
  
  
if __name__ == '__main__':
    main()
