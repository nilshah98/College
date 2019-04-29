"""

t = a-b
u = a-c
v = t+u
d = v+u
"""

n_reg = int(input("Enter the number of registers: "))

register_descriptor = dict()
address_descriptor = list()
results = []

for i in range(n_reg):
	register_descriptor["R"+str(i)] = ""



def getreg(operand, pres):
	"""
	1/0 - found, not found(show nearest avb.)
	-1 - no empty space( show nearest swap), swap to operand_table and give reg + add to result
	return reg
	"""
	global register_descriptor, results, address_descriptor
	
	if pres == 1:
		flag = 10**5
		for k in register_descriptor.keys():
			if register_descriptor[k] == operand:
				register_descriptor[k] = operand
				return k
			elif register_descriptor[k] == "":
				flag = min(flag,int(k[1:]))
		
		if flag == 10**5:
			reg_temp = list(register_descriptor.keys())[0]
			address_descriptor.append(register_descriptor[reg_temp])
			print("MOV "+reg_temp + ", " + register_descriptor[reg_temp])
			register_descriptor[reg_temp] = ""
			print("ADD DESC: ", address_descriptor)
			print("REG DESC: ", register_descriptor)
			print()
			results.append("MOV "+reg_temp + ", " + register_descriptor[reg_temp])	# memory
			print("MOV "+operand + ", " + reg_temp)
			register_descriptor[reg_temp] = operand
			print("ADD DESC: ", address_descriptor)
			print("REG DESC: ", register_descriptor)
			print()
			results.append("MOV "+operand + ", " + reg_temp)
			return reg_temp	
		else:
			register_descriptor["R"+str(flag)] = operand
			print("MOV "+operand + ", " + "R"+str(flag))
			print("ADD DESC: ", address_descriptor)
			print("REG DESC: ", register_descriptor)
			print()
			results.append("MOV "+operand + ", " + "R"+str(flag))
			return "R"+str(flag)
	else:
		for k in register_descriptor.keys():
			if register_descriptor[k] == operand:
				return k
		return -1

three_address = open("inputs_cg.txt","r")
lines = three_address.readlines()
n_lines = len(lines)

for i, line in enumerate(lines):
	assign,ops = line[:-1].split("=")
	assign = assign.strip()
	ops = ops.strip()
	if "-" in ops:
		op1,op2 = ops.split("-")
		op = "SUB"
	elif "+" in ops:
		op1,op2 = ops.split("+")
		op = "ADD"
	elif "*" in ops:
		op1,op2 = ops.split("*")
		op = "MUL"
	elif "/" in ops:
		op1,op2 = ops.split("/")
		op = "DIV"
	else:
		print("INVALID OPERATION")
	
	register1 = getreg(op1, 1)
	register2 = getreg(op2, 2)
	# Add to result with op
	if register2 == -1:
		print(op + " " + op2 + ", " + register1)
		results.append(op + " " + op2 + ", " + register1)
	else:
		print(op + " " + register2 + ", " + register1)
		results.append(op + " " + register2 + ", " + register1)
	
	register_descriptor[register1] = assign
	if i == n_lines - 1:
		print("MOV "+register1 + ", " + assign)
		address_descriptor.append(assign)
		register_descriptor[register1] = ""
		print("ADD DESC: ", address_descriptor)
		print("REG DESC: ", register_descriptor)
		print()
	print("-"*100)


