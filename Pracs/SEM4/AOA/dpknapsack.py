#taking inputs here -
print("Enter the weights of the items")
weights = list(map(int, input().split()))
print("Enter the profits of the items")
profits = list(map(int, input().split()))
print("Enter the amount of weight allowed")
bound = int(input())

#linking profits with weight, so that they remain together while sorting
for i in range(len(profits)):
	temp = [weights[i],profits[i]]
	profits[i] = temp

#sorting weights and profits
weights.sort()
profits.sort()

#creating and updating the table here
#cols will contain weights starting from 0 to bound
#rows will contain weights of the items in the bag

#initialising all elements to 0 here
table = [[0 for _ in range(bound+1)] for _ in range(len(weights))]

for i in range(len(weights)):
	for j in range(bound+1):
		#checking if earlier items present in bag to compare with, or first item
		if i>0:
			#if items already present, check if current item can fit into the bag, ie. current bound - weight[i] > 0
			if (j-weights[i])>=0:
				table[i][j] = max(table[i-1][j-weights[i]]+profits[i][1], table[i-1][j])
			#if item doesn't fit, then carry over the item from top
			else:
				table[i][j]=table[i-1][j]
		#if it is the first item to be put into the bag, check if it's weight is more than the bound, and add it
		elif j>=weights[i]:
			table[i][j]=profits[i][1]
		#it item not added, let it be 0

print("Table so formed:")
for i in range(len(weights)):
	print(*table[i])

maxProfit = table[len(weights)-1][bound]
print("Max profit is",maxProfit)

#backtracking part
contentBag = []

i = len(weights)-1
j = bound

while(i>=0 and j>=0):
	if i>0:
		if table[i][j]==table[i-1][j]:
			i-=1
		else:
			contentBag.append(weights[i])
			i-=1
			j-=contentBag[-1]

	if i==0:
		if table[i][j]>0:
			contentBag.append(weights[i])
		i-=1

print("the weight content of the bag is:")
print(*contentBag)

#Mistakes done:
#1. instead of profits added weight, in the compare loop
#2. need to check if item can fit in bag, ie. j-weights[i]>0
#3. Need to take input in sorted by weight order
#4. While backtracking for edge condition ie. 1, if value at that point is not greater than 0, still decrement i