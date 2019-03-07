import random
for i in range(50):
	nodeGenX = '$node_(' + str(i) + ')	set X_ ' + str(random.randint(1,450))
	nodeGenY = '$node_(' + str(i) + ')	set Y_ ' + str(random.randint(1,450))
	nodeGenZ = '$node_(' + str(i) + ')	set Z_ ' + str(0)
	print(nodeGenX)
	print(nodeGenY)
	print(nodeGenZ)

	nodeMove = '$ns_ at ' + str(random.randint(1,125)) + ' "$node_('+ str(i) +') setdest ' + str(random.randint(1,450)) + " " + str(random.randint(1,450)) + " " + str(0) + '"'
	print(nodeMove)
