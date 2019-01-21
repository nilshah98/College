#=================TOKENS================================
keywords = {
"variable":[],
"headerfile":[],
"function":[],
"operation":[],
}

special = []

dataTypes = ["int","char","float","bool","void"]
operators = ["=","+","-","*","/"]
#=================READ C FILE=========================== 
f = open("./hello.c")
program = f.read()
f.close

#=================SPLIT BY LINE=========================
programLines = program.split(";")
lineNum = 0
for line in programLines:
    newLines = line.split("\n")
    for line in newLines:
	if len(line)>0:
		lineNum += 1
	else:
		continue
        if len(line)>0 and line[0] == "#":
            keywords["headerfile"].append([lineNum,line])
        else:
            tokens = line.split()
            if len(tokens)>0 and tokens[0] in dataTypes:
                if "(" and ")" in line:
                    keywords["function"].append([lineNum,line])
                else:
                    variables = tokens[1].split(",")
                    for var in variables:
                        keywords["variable"].append([lineNum,var])
            else:
                if "(" and ")" in line:
                    keywords["function"].append([lineNum,line])
                else:
                    keywords["operation"].append([lineNum,line])

for key in keywords.keys():
	print(key+"--->")
	for token in keywords[key]:
		if len(token[1])>0 and token[1] != "," and token[1] != "''" and token[1] !="{" and token[1] != "}":
			print(token)
		else:
			special.append(token)
	print("==============================================")
print("special--->")
for i in special:
	print(i)
