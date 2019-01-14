#=================TOKENS================================
keywords = {
"variable":[],
"headerfile":[],
"function":[],
"condition":[],
"loop":[]
}

#=================READ C FILE=========================== 
f = open("./hello.c")
program = f.read()
f.close

#=================SPLIT BY LINE=========================
programLines = program.split("\n");
print(programLines)

#=================SPLIT BY SPACE========================
varfunc = False
header = False
operator = False
condition = False
loop = False
for line  in programLines:
	tokens = line.split(" ",1)
	for keyword in tokens:
		#print(keyword, varfunc, header, condition, loop)
		if keyword == "int" or keyword == "float" or keyword =="char" or keyword == "void" or keyword == "bool":
			varfunc = True
		elif len(keyword)>0 and keyword[0] == "#":
			header = True
		elif keyword == "if" or keyword == "else":
			condition = True
		elif keyword == "for" or keyword == "while":
			loop = True
		elif varfunc:
			if "(" and ")" in keyword:
				keywords["function"].append(keyword)
				varfunc = False
			elif "," in keyword:
				for i in keyword.split(","):
					keywords["variable"].append(i)
				varfunc = False
		elif loop:
			keywords["loop"].append(keyword)
			loop = False
		elif condition:
			keywords["condition"].append(keyword)
			condition = False
		elif header:
			keywords["headerfile"].append(keyword)
			header = False
		elif "(" and ")" in keyword:
			keywords["function"].append(keyword)

print(keywords)
