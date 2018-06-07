#N-Queens problem

#checking functionj
def checkIfPoss(x,y,board):
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] and (x==col or y==row or abs(x-col)==abs(y-row)) and not(x==col and y==row):
				return False
	
	return True

def NQueens(n):
	#mark the regions here
	marked = [0 for i in range(n**2)]
	#create board here, and initialise all to 0
	board = [[0 for _ in range(n)] for _ in range(n)]
	#initialise flag, inital row, and solution
	row = 0
	sol = 1
	flag = True

	while flag:
		
		#while flag
		#initalise col here
		col = 0

		#check to see, if any one's already in the column, if yes, set col, one next to it
		for colx in range(len(board[row])):
			if board[row][colx]:
				board[row][colx] = 0
				col = colx + 1

		while col < n:
			#mark the visited cell
			marked[row*n + col] = 1
			
			#check if current cell is feasible, if yes, mark and break
			if checkIfPoss(col,row,board):
				board[row][col] = 1
				break
			col += 1

			#condition for breaking, all the cells are marked, ie. last cell to be marked will be marked[0][n-1], since backtracking
			#now after last cell is visited, backtrack for it, final condition, last cell of second row
			# if row == 1 and col == n and sum(marked)==n**2:
				# flag = False

		#check if any location found -
		#if sum of row is 1, 1 is there init

		#else, when first row and col is n
		if row == 0 and col == n:
			flag = False
		if sum(board[row]) == 1:
			sumOfboard = 0
			
			for rowx in board:
				sumOfboard += sum(rowx)
			
			#if sum of board is euqal to n, there are n queens
			if sumOfboard == n:
				print("Solution number",sol)
				for rowx in board:
					print(*rowx)
				print()
				sol += 1
			row += 1

			#if row = n reached, decrement it, and find other solutions
			if row == n:
				row -= 1

		#else backtrack
		else:
			row -= 1


	# print(marked)

print("Enter the number of queens")
n = int(input())
NQueens(n)