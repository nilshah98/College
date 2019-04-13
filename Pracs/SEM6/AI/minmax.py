import copy

class TicTacToe:
    def __init__(self,board):
        self.board = board
        self.cost = 0
    
    def __str__(self):
        printString = ""
        for i in range(9):
            printString+= str(self.board[i])
            printString+=" | "
            if i%3 == 2:
                printString+="\n"
        return printString
    
    def mark(self,loc):
        Xcount = 0
        Ocount = 0
        for i in range(9):
            if self.board[i] == "X":
                Xcount +=1
            elif self.board[i] == "O":
                Ocount += 1
        if Xcount - Ocount > 1 or Xcount - Ocount  < 0:
            raise Exception("Invalid board state")
        else:
            if Xcount - Ocount == 1:
                sign = "O"
            else:
                sign = "X"
            if self.board[loc] == " ":
                self.board[loc] = sign
            else:
                raise Exception("Place already filled")
    
    def getFreeLoc(self):
        locs = []
        if not self.calcCost():
            for i in range(9):
                if self.board[i] == " ":
                    locs.append(i)
        return locs
    
    def calcCost(self):
        if self.board[0] == self.board[1] == self.board[2]:
            if self.board[0] == "X":
                self.cost = 10
            elif self.board[0] == "O":
                self.cost = -10
            return True
        elif self.board[3] == self.board[4] == self.board[5]:
            if self.board[3] == "X":
                self.cost = 10
            elif self.board[3] == "O":
                self.cost = -10
            return True
        elif self.board[6] == self.board[7] == self.board[8]:
            if self.board[6] == "X":
                self.cost = 10
            elif self.board[6] == "O":
                self.cost = -10
            return True
        elif self.board[0] == self.board[3] == self.board[6]:
            if self.board[0] == "X":
                self.cost = 10
            elif self.board[0] == "O":
                self.cost = -10
            return True
        elif self.board[1] == self.board[4] == self.board[7]:
            if self.board[1] == "X":
                self.cost = 10
            elif self.board[1] == "O":
                self.cost = -10
            return True
        elif self.board[2] == self.board[5] == self.board[8]:
            if self.board[2] == "X":
                self.cost = 10
            elif self.board[2] == "O":
                self.cost = -10
            return True
        elif self.board[0] == self.board[4] == self.board[8]:
            if self.board[0] == "X":
                self.cost = 10
            elif self.board[0] == "O":
                self.cost = -10
            return True
        elif self.board[2] == self.board[4] == self.board[6]:
            if self.board[2] == "X":
                self.cost = 10
            elif self.board[2] == "O":
                self.cost = -10
            return True
'''
__init__
__str__
mark
getFreeLoc
calcCost
'''

initState = ["X"," ","X","O","O"," ","X","O"," "]
initBoard = TicTacToe(initState)
initBoard.calcCost

states = [initBoard]
bfsQueue = [initBoard]

while len(bfsQueue) > 0:
    parentBoard = bfsQueue[0]
    currLocs = parentBoard.getFreeLoc()
    if len(currLocs) > 0:
        for i in currLocs:
            currBoard = TicTacToe(copy.deepcopy(parentBoard.board))
            currBoard.mark(i)
            currBoard.calcCost()
            states.append(currBoard)
            bfsQueue.append(currBoard)
    bfsQueue = bfsQueue[1:]

for i in states:
    print(i)
    print(i.cost)
    print("============================================")
