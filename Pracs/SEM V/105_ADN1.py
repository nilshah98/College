print("Enter your IP address:")
ip = raw_input()
nums = ip.split(".")
poss = True
# CHECKING ONLY 4 BLOCKS ENTERED
if len(nums) != 4:
	poss = False

# CHECKING ALL VALS ARE INTEGERS
if poss:
	for i in nums:
		try:
			int(i)
		except:
			poss = False

# CHECKING FOR VALUES BETWEEN 0 AND 255
if poss:
	for i in nums:
		if int(i) < 0 or int(i) > 255:
			poss = False

# CHECKING NO 0's ADDED AT START
if poss:
	for i in nums:
		if len(str(int(i))) != len(i):
			poss = False

if poss:
	print("Valid IP address")
else:
	print("Not valid IP address")

"""
IP CLASSES

CLASS | SRT | END
===================
A     | 0   | 127 
B     | 128 | 191 
C     | 192 | 223 
D     | 224 | 239 
E     | 240 | 255 

CLASS | NET ID  | HOST ID
=========================
A     |  8 BITS | 24 BITS
B     | 16 BITS | 16 BITS 
C     | 24 BITS |  8 BITS
D     | -       | -
E     | -       | -
"""

# IDENTIFYING CLASSES

if poss:
	start = ".0.0.0"
	final = ".255.255.255"
	first = int(nums[0])
	if first >= 0 and first <= 127:
		print("Class A")
		print("Block Start:")
		print(nums[0]+start[:])
		print("Block Ends:")
		print(nums[0]+final[:])

	elif first >= 128 and first <= 191:
		print("Class B")
		print("Block Start:")
		print(nums[0]+"."+nums[1]+start[2:])
		print("Block Ends:")
		print(nums[0]+"."+nums[1]+final[4:])

	elif first >= 192 and first <= 223:
		print("Class C")
		print("Block Start:")
		print(nums[0]+"."+nums[1]+"."+nums[2]+start[4:])
		print("Block Ends:")
		print(nums[0]+"."+nums[1]+"."+nums[2]+final[8:])

	elif first >= 224 and first <= 239:
		print("Class D")
	else:
		print("Class E")