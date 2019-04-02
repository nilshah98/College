import copy

goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
goalDict = {0: [0, 0],
            1: [0, 1],
            2: [0, 2],
            3: [1, 0],
            4: [1, 1],
            5: [1, 2],
            6: [2, 0],
            7: [2, 1],
            8: [2, 2]
            }
# ======================= UTILITY FUNCTIONS ===========================

# Check whether 2 matrix same


def check(stateSpace, temp):
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
	def __init__(self, puzzle, blankRow, blankCol, level):
		self.puzzle = puzzle
		self.blankRow = blankRow
		self.blankCol = blankCol
		self.normCost = 0
		self.manhattan = 0
		self.level = level

	# Print puzzle
	def __str__(self):
		printString = ""
		for i in range(3):
			for j in range(3):
				printString += str(self.puzzle[i][j])
				printString += " | "
			printString += "\n"
		printString += "Manhattan Cost : " + str(self.manhattan) + "\n"
		printString += "Normal Cost : " + str(self.normCost) + "\n"
		printString += "Level : " + str(self.level) + "\n"
		return printString

	def calcManhattan(self):
		cost = 0
		for i in range(3):
			for j in range(3):
				val = self.puzzle[i][j]
				cost += abs(goalDict[val][0] - i)
				cost += abs(goalDict[val][1] - j)
		self.manhattan = cost
	
	def calcNormCost(self):
		cost = 0
		for i in range(3):
			for j in range(3):
				val = self.puzzle[i][j]
				if(goalState[i][j] != val):
					cost += 1
		self.normCost = cost

	# Move blank piece up
	def moveup(self):
		if self.blankRow == 0:
			return False
		else:
			self.level += 1
			self.puzzle[self.blankRow-1][self.blankCol],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow-1][self.blankCol]
			self.blankRow -= 1
			return True

	# Move blank piece down
	def movedown(self):
		if self.blankRow == 2:
			return False
		else:
			self.level += 1
			self.puzzle[self.blankRow+1][self.blankCol],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow+1][self.blankCol]
			self.blankRow += 1
			return True

	# Move blank piece left
	def moveleft(self):
		if self.blankCol == 0:
			return False
		else:
			self.level += 1
			self.puzzle[self.blankRow][self.blankCol-1],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow][self.blankCol-1]
			self.blankCol -= 1
			return True

	# Move blank piece right
	def moveright(self):
		if self.blankCol == 2:
			return False
		else:
			self.level += 1
			self.puzzle[self.blankRow][self.blankCol+1],self.puzzle[self.blankRow][self.blankCol] = self.puzzle[self.blankRow][self.blankCol],self.puzzle[self.blankRow][self.blankCol+1]
			self.blankCol += 1
			return True


# =================== DRIVER FUNCTION =================================

def solve():
	puzzle = [[0,0,0] for i in range(3)]
	for i in range(3):
		for j in range(3):
			print("Enter values for row:"+str(i)+" col:" + str(j))
			puzzle[i][j] = int(input())

	print("Enter location of blank space")
	blankRow = int(input())
	blankCol = int(input())
	Puzzlex = Puzzle(puzzle,blankRow,blankCol,0)

	bfsQueue = [Puzzlex]

	stateSpaceTree = [Puzzlex]
	goal = "notfound"

	# up,down,left,right
	while goal == "notfound":
		
		print()
		
		# Next puzzle to be expanded =>
		print(bfsQueue[0],end="==========================>\n\n")
		
		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol,bfsQueue[0].level)
		if(tempPuzzle.moveup()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				tempPuzzle.calcManhattan()
				tempPuzzle.calcNormCost()
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("moveup")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					goal = "found"
					break

		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol,bfsQueue[0].level)
		if(tempPuzzle.movedown()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				tempPuzzle.calcManhattan()
				tempPuzzle.calcNormCost()
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("movedown")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					goal = "found"
					break

		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol,bfsQueue[0].level)
		if(tempPuzzle.moveleft()):
			flag = False
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				tempPuzzle.calcManhattan()
				tempPuzzle.calcNormCost()
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("moveleft")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					goal = "found"
					break

		tempPuzzle = Puzzle(copy.deepcopy(bfsQueue[0].puzzle),bfsQueue[0].blankRow,bfsQueue[0].blankCol,bfsQueue[0].level)
		print(tempPuzzle.level)
		if(tempPuzzle.moveright()):
			flag = False
			print(tempPuzzle.level)
			for i in stateSpaceTree:
				if(check(i.puzzle, tempPuzzle.puzzle)):
					flag = True
					break
			if(not flag):
				tempPuzzle.calcManhattan()
				tempPuzzle.calcNormCost()
				bfsQueue.append(tempPuzzle)
				stateSpaceTree.append(tempPuzzle)
				print("moveright")
				print(tempPuzzle)
				if(check(goalState,tempPuzzle.puzzle)):
					print("goalStateFound")
					goal = "found"
					break
		
		# Removing the traversed state from queue
		bfsQueue = bfsQueue[1:]
		print("------------------------------------")

solve()
