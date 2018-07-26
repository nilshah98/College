import math
# TAKING IP AS INPUT
print("Enter classless ip-")
ip = input().split(".")
classlessIp = []
for i in range(4):
	if i != 3:
		classlessIp.append(int(ip[i]))
	else:
		fin,subnetLen = ip[i].split("/")
		classlessIp.append(int(fin))
		subnetLen = int(subnetLen)

# TAKING BLOCKS AS INPUT
print("Enter number of blocks")
noBlocks = int(input())
blocks = []
print("Enter sizes for each block")
for i in range(noBlocks):
	print("Enter size of " + str(i+1) + " block")
	blocks.append(int(input()))

# SORTING THE BLOCKS AS PER SIZE
blocks.sort(reverse = True)

# FINDING THE BEGINNING ADDRESS OF FIRST BLOCK
# FUNCTION TO CONVERT SUBNET LENGTH TO DEC IPS 24 -> 255.255.255.0
def getSubNet(n):
	subnet = []
	full = n//8
	rem = n%8
	last = 0
	for i in range(full):
		subnet.append(255)
	for i in range(rem):
		last += (2**(8-i-1))
	subnet.append(last)
	return subnet

defaultSubnet = getSubNet(subnetLen)

# GET SUBNET AND MASK FOR EACH BLOCK
# GET CLOSEST POWER
def getClosestPower(n):
	temp = math.log(n,2)
	if temp%1:
		temp = int(temp) + 1
	else:
		temp = int(temp)
	return temp

def getCompSubNetBits(s):
	s = list(s)
	temp = []
	for i in range(4):
		curr = 0
		for j in range(8):
			x = s.pop()
			if int(x):
				curr += 2**j
		temp.append(curr)
	temp = temp[::-1]
	return temp

blocksSubnetLength = []
blocksSubNet = []
for i in blocks:
	length = getClosestPower(i)
	blocksSubnetLength.append(32-length)
	blockSub = "0"*(32-length)
	blockSub += "1"*length
	blocksSubNet.append(getCompSubNetBits(blockSub))


# GATHERED DATA
print(*classlessIp)
print(defaultSubnet)
print(*blocksSubnetLength)
print(*blocksSubNet)

startAddress = []
for i in range(4):
	startAddress.append(classlessIp[i] & defaultSubnet[i])

# print(startAddress)

for i in range(noBlocks):
	print("Starting address for block "+str(i+1))
	print(".".join(map(str,startAddress)) + "/" + str(blocksSubnetLength[i]))
	endAddress = []
	for j in range(4):
		endAddress.append(startAddress[j] | blocksSubNet[i][j])
	print("Ending address for block "+str(i+1))
	print(".".join(map(str,endAddress)) + "/" + str(blocksSubnetLength[i]))
	print("====================================")
	endAddress[-1] += 1
	startAddress = endAddress
