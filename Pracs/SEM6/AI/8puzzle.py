import copy
class Puzzle:
	def __init__(self,puzzle,blankRow,blankCol):
		self.puzzle = puzzle
		self.blankRow = blankRow
		self.blankCol = blankCol

	def __str__(self):
		printString = ""
		for i in range(3):
			for j in range(3):
				printString+= str(self.puzzle[i][j])
				printString+=" | "
			printString+="\n"
		return printString


	def moveup(self):
		if self.blankRow ==0:
			return False
		else:
			self.puzzle[self.blankRow-1][self.blankCol],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow-1][self.blankCol]
			self.blankRow -= 1
			return True

	def movedown(self):
		if self.blankRow == 2:
			return False
		else:
			self.puzzle[self.blankRow+1][self.blankCol],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow+1][self.blankCol]
			self.blankRow += 1
			return True

	def moveleft(self):
		if self.blankCol == 0:
			return False
		else:
			self.puzzle[self.blankRow][self.blankCol-1],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow][self.blankCol-1]
			self.blankCol -= 1
			return True

	def moveright(self):
		if self.blankCol == 2:
			return False
		else:
			self.puzzle[self.blankRow][self.blankCol+1],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow][self.blankCol+1]
			self.blankCol += 1
			return True

def visited(stateSpace,temp):
	for i in range(3):
		for j in range(3):
			if stateSpace[i][j] == temp[i][j]:
				continue
			else:
				return False
	return True

def solve():
	puzzle = [[0,0,0] for i in range(3)]
	for i in range(3):
		for j in range(3):
			print("Enter values for "+str(i)+" row")
			print("Enter values for "+str(j)+"col")
			puzzle[i][j] = int(input())

	print("Enter location of blank space")
	blankRow = int(input())
	blankCol = int(input())
	Puzzlex = Puzzle(puzzle,blankRow,blankCol)
	print(Puzzlex)

	stateSpace = [Puzzlex]
	initialState = [Puzzlex]
	bfsQueue = [Puzzlex]

	#up,down,left,right
	tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
	if(tempPuzzle.moveup()):
		bfsQueue.append(tempPuzzle)

	tempPuzzlex = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
	if(tempPuzzlex.movedown()):
		bfsQueue.append(tempPuzzlex)

	tempPuzzley = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
	if(tempPuzzley.moveleft()):
		bfsQueue.append(tempPuzzley)

	tempPuzzlez = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
	if(tempPuzzlez.moveright()):
		bfsQueue.append(tempPuzzlez)

	for i in bfsQueue:
		print(i)

solve()
