print("Enter first string to find lcs")
str1 = input()
print("Enter second string to find lcs")
str2 = input()

#creating table here, column contents will be of str1 and row contents will be of str2
#also appending an extra first row and column of 0's so as to compare earlier stages if no match
table = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

#updating the table here
for i in range(1,len(str2)+1):
	for j in range(1,len(str1)+1):
		if str2[i-1]==str1[j-1]:
			table[i][j]=table[i-1][j-1]+1
		else:
			table[i][j]=max(table[i-1][j],table[i][j-1])

print("LCS table is:")
for i in range(len(str2)+1):
	print(*table[i])

print("LCS length is:")
print(table[len(str2)][len(str1)])


#backtracking for 1 LCS
# LCS=[]

# i = len(str2)
# j = len(str1)

# while i!=0 and j!=0:
# 	#case 1: current character is same
# 	if table[i][j]>table[i-1][j] and table[i][j]>table[i][j-1]:
# 		LCS.append(str1[j-1])
# 		j-=1
# 		i-=1
# 	#case2: the above row same col, has higher val
# 	elif table[i-1][j]>table[i][j-1]:
# 		i-=1
# 	#case3: the same row above col, has higher val
# 	else:
# 		j-=1
# # print("LCS is:")
# # print("".join(LCS[::-1]))

i = len(str2)
j = len(str1)

#backtrack for all LCS's
def backtrack(i,j):
	allLCS = []
	if i>0 and j>0:
		#case1 both the characters are equal
		if str1[j-1]==str2[i-1]:
			temp = backtrack(i-1,j-1)
			#if length greater than 0, add earlier backtrack with new character
			if len(temp)>0:
				for lcs in temp:
					allLCS.append(lcs+str1[j-1])
			#if length less than 0, initialise with the equal character
			else:
				allLCS.append(str1[j-1])

		#case2 they aren't equal
		else:
			#if one of the branches, ie up or left, exclusively bigger, backtrack through that branch
			if table[i-1][j]>table[i][j-1]:
				allLCS = backtrack(i-1,j)
			elif table[i-1][j]<table[i][j-1]:
				allLCS = backtrack(i,j-1)
			#if noth equal, go and both branch, and combine their results
			else:
				temp1 = backtrack(i-1,j)
				temp2 = backtrack(i,j-1)
				for lcs in temp1:
					allLCS.append(lcs)
				for lcs in temp2:
					allLCS.append(lcs)	
	return allLCS

allLCS = backtrack(i,j)
print(*allLCS)