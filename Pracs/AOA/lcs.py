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


#backtracking
LCS=[]

i = len(str2)
j = len(str1)


#Mistakes
#1. since no 0 appended at start of strings, we need to decremenet 1, while comparing them