import random
def sequential(files, blocks):
	locations = [0]*blocks
	if(sum(files) > blocks):
		print("Not enough space to allocate memory")
	else:
		currfile = 1
		currloc = 0
		for i in files:
			skip = random.randint(0,3)
			currloc += skip
			while( currloc + i-1 >= blocks ):
				currloc -= skip
				skip = random.randint(0,3)
				currloc += skip
			for j in range(currloc, currloc + i):
				locations[j] = currfile
			currloc += i+1
			currfile += 1
		print("The file allocated are for sequenctial- ")
		print(*locations)

def chained(files, blocks):
	locations = [0]*blocks
	done = set()
	if(sum(files) > blocks):
		print("Not enough space to allocate memory")
	else:
		currfile = 1
		for i in range(0,len(files)):
			#get start loc
			loc = 0
			while(loc in done):
				loc = random.randint(0, blocks - 1)
			done.add(loc)

			#get next loc
			nxt = 0
			todo = files[i]
			while(todo > 0):
				if todo == 1:
					locations[loc] = [currfile, -1]
					currfile += 1
					todo -= 1
				else:
					while(nxt in done):
						nxt = random.randint(0,blocks-1)
					done.add(nxt)
					locations[loc] = [currfile,nxt]
					loc = nxt
					todo -= 1
		print("The files allocated in chained are- ")
		print(*locations)
				
def indexed(files, blocks):
	locations = [0]*blocks
	done = set()
	if(sum(files)+len(files) > blocks):
		print("Not enough space to allocate memory")
	else:
		currfile = 1
		for i in range(0,len(files)):
			home = -1

			#get start loc
			loc = 0
			while(loc in done):
				loc = random.randint(0, blocks - 1)
			done.add(loc)

			todo = files[i]
			flag = True
			seq = 0
			while(todo > 0):
				if flag:
					home = loc
					locations[home] = [currfile]
					flag = False
				else:
					seq += 1
					while(loc in done):
						loc = random.randint(0,blocks-1)
					done.add(loc)
					locations[loc] = currfile
					locations[home].append([seq,loc])
					todo -= 1
			currfile += 1
		print("The files allocated in indexed are- ")
		print(*locations)
	

print("Enter number of files to be managed")
n = int(input())
print("Enter space separated file blocks needed")
files = list(map(int, input().split()))
print("Enter total blocks in secondary memory")
blocks = int(input())

sequential(files, blocks)
chained(files, blocks)
indexed(files,blocks)
