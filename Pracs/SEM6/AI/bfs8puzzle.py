import copy

goalState = [[0,1,2],[3,4,5],[6,7,8]]

# ======================= UTILITY FUNCTIONS ===========================

# Check whether 2 matrix same
def check(stateSpace,temp):
	for i in range(3):
		for j in range(3):
			if stateSpace[i][j] == temp[i][j]:
				continue
			else:
				return False
	return True

# ======================= PUZZLE CLASS ===========================

class Puzzle:

	# Initialise puzzle
	def __init__(self,puzzle,blankRow,blankCol):
		self.puzzle = puzzle
		self.blankRow = blankRow
		self.blankCol = blankCol

	# Print puzzle
	def __str__(self):
		printString = ""
		for i in range(3):
			for j in range(3):
				printString+= str(self.puzzle[i][j])
				printString+=" | "
			printString+="\n"
		return printString


	# Move blank piece up
	def moveup(self):
		if self.blankRow ==0:
			return False
		else:
			self.puzzle[self.blankRow-1][self.blankCol],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow-1][self.blankCol]
			self.blankRow -= 1
			return True

	# Move blank piece down
	def movedown(self):
		if self.blankRow == 2:
			return False
		else:
			self.puzzle[self.blankRow+1][self.blankCol],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow+1][self.blankCol]
			self.blankRow += 1
			return True

	# Move blank piece left
	def moveleft(self):
		if self.blankCol == 0:
			return False
		else:
			self.puzzle[self.blankRow][self.blankCol-1],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow][self.blankCol-1]
			self.blankCol -= 1
			return True

	# Move blank piece right
	def moveright(self):
		if self.blankCol == 2:
			return False
		else:
			self.puzzle[self.blankRow][self.blankCol+1],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow][self.blankCol+1]
			self.blankCol += 1
			return True


# =================== DRIVER FUNCTION =================================

def solve():
	puzzle = [[0,0,0] for i in range(3)]
	for i in range(3):
		for j in range(3):
			print("Enter values for "+str(i)+" row")
			print("Enter values for "+str(j)+" col")
			puzzle[i][j] = int(input())

	print("Enter location of blank space")
	blankRow = int(input())
	blankCol = int(input())
	Puzzlex = Puzzle(puzzle,blankRow,blankCol)

	stateSpace = [Puzzlex]
	bfsQueue = [Puzzlex]

	stateSpaceTree = [Puzzlex]

	#up,down,left,right
	while len(bfsQueue)>0:
		
		print()
		print(bfsQueue[0],end="===>\n")
		
		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
		if(tempPuzzle.moveup()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("moveup")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					break

		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
		if(tempPuzzle.movedown()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("movedown")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					break

		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
		if(tempPuzzle.moveleft()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("moveleft")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					break

		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol)
		if(tempPuzzle.moveright()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("moveright")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					break
		
		bfsQueue = bfsQueue[1:]
		print("------------------------------------")

solve()
