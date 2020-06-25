class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        # TO DO: delete pass (and this comment) and complete method
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass (and this comment) and complete method
        print("   0   1   2")
        index = 0
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    rowList.append(' ')
                else:
                    rowList.append(self.board[row][col])
            print("{0}  {1} | {2} | {3}  ".format(index,rowList[0],rowList[1],rowList[2]))
            if index != 2:
                print("  -----------")
            index = index + 1


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    
    def update(self, row, col, mark):
        '''
        Assigns the integer, mark, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        print(self.squareIsEmpty(row,col))
        if self.squareIsEmpty(row,col):
            self.board[row][col] = mark
            return True
        else:
            return False
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    return False
        return True
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        rowWin = False
        for row in range(len(self.board)):
            myList = []
            for col in range(len(self.board)):
                myList.append(self.board[row][col])
            if sum(myList) == 15:
                rowWin = True

        colWin = False
        for col in range(len(self.board)):
            column = []
            for row in range(len(self.board)):
                column.append(self.board[row][col])
            if sum(column) == 15:
                colWin = True

        diagWin = False
        diagonal1 =[]
        diagonal2 = []
        for index in range(len(self.board)):
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][len(self.board) - index - 1]
            diagonal2.append(tile)

        if sum(diagonal1) == 15 or sum(diagonal2) == 15:
            diagWin = True

        if diagWin == True or colWin == True or rowWin == True:
            return True
        else:
            return False
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        # TO DO: delete pass (and this comment) and complete method
        return True        
    
    
class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        # TO DO: delete pass (and this comment) and complete method
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
               
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass (and this comment) and complete method
        print("   0   1   2")
        index = 0
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    rowList.append(' ')
                else:
                    rowList.append(self.board[row][col])
            print("{0}  {1} | {2} | {3}  ".format(index,rowList[0],rowList[1],rowList[2]))
            if index != 2:
                print("  -----------")
            index = index + 1


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        print(self.squareIsEmpty(row,col))
        if self.squareIsEmpty(row,col):
            self.board[row][col] = mark
            return True
        else:
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    return False
        return True
        
           
    def isWinner(self):
        
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''     
        for row in range(self.size):
            for col in range(self.size):
                
                if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.squareIsEmpty(0,col) == False:
                    return True
                if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.squareIsEmpty(row,0) == False:
                    return True
                if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.squareIsEmpty(0,0) == False:
                    return True
                if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.squareIsEmpty(1,1) == False:
                    return True
        return False
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        # TO DO: delete pass (and this comment) and complete method
        return False


class MetaTicTacToe:
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''       
        # TO DO: delete pass (and this comment) and complete method
        self.size = 3
        self.board = []
        filename = open(configFile,'r')
        self.board = filename.readlines()
        for row in range(self.size):
           self.board[row] = self.board[row].strip().split()
           
               
        #print(self.board)
                
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass (and this comment) and complete method
        print("   0   1   2")
        index = 0
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board)):
                
                if self.board[row][col] == 0:
                    rowList.append('')
                else:
                    rowList.append(self.board[row][col])
            print("{0}  {1} | {2} | {3}   ".format(index,rowList[0],rowList[1],rowList[2]))
            if index != 2:
                print("  -----------")
            index = index + 1


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.board[row][col] == 'c' or self.board[row][col] == 'n':
            return True
        else:
            return False
    
    
    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        print(self.squareIsEmpty(row,col))
        if self.squareIsEmpty(row,col):
            self.board[row][col] = result
            return True
        else:
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == "c" or self.board[row][col] == "n":
                    return False
                
                #if self.board[row][col] == 0:
                 #   return False
        return True

   
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        for row in range(self.size):
            for col in range(self.size):
                
                if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.squareIsEmpty(0,col) == False:
                    return True
                if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.squareIsEmpty(row,0) == False:
                    return True
                if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.squareIsEmpty(0,0) == False:
                    return True
                if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.squareIsEmpty(1,1) == False:
                    return True
        return False
    
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        # TO DO: delete pass (and this comment) and complete method
        print(self.squareIsEmpty(row,col))
        if self.squareIsEmpty(row,col):
            if self.board[row][col] == 'c':
                return(ClassicTicTacToe())
            else:
                return(NumTicTacToe())
        return None
                          
if __name__ == "__main__":
    # TEST EACH CLASS THOROUGHLY HERE   
    num = NumTicTacToe()
    classic = ClassicTicTacToe()
    meta = MetaTicTacToe('MetaTTTconfig.txt')
    
    #testing for squareIsEmpty and update and isWinner and boardFull and isNum functions in NumTicTacToe class

    #print(num.squareIsEmpty(0,0))
    #num.update(0,0,1)
    #print(num.boardFull())
    #print(num.squareIsEmpty(0,0))
    #print(num.isWinner())
    #num.update(0,1,9)
    #num.update(0,2,5)
    #print(num.isWinner())
    #num.update(2,2,1)
    #print(num.isNum())
    
    
    #testing for squareIsEmpty and update and isWinner and boardFull and isNum functions in ClassicTicTacToe class
    
    #print(classic.squareIsEmpty(0,0))
    #classic.update(0,0,'O')
    #print(classic.boardFull())
    #print(classic.squareIsEmpty(0,0))
    #classic.update(0,1,'O')
    #classic.update(0,2,'O')
    #print(classic.isWinner())
    #print(classic.isNum())
    
    #testing for squareIsEmpty and update and isWinner and boardFull and getLocalBoard in MetaTicTacToe class
    
    #print(meta.squareIsEmpty(0,0))
    #meta.update(0,0,'O')
    #print(meta.boardFull())
    #print(meta.squareIsEmpty(0,0))
    #meta.update(0,1,'O')
    #meta.update(0,2,'O')
    #print(meta.isWinner())
    #print(meta.getLocalBoard(1,1)) #prints num tic tac toe because at position (1,1) n is stored 
    #print(meta.getLocalBoard(0,0)) #prints class tic tac toe because at position (0,0) c is stored
    

                
                
    
            

           
