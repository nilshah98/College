import re
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
uid = 0
for line in programLines:
    newLines = line.split("\n")
    for line in newLines:
	if len(line)>0:
		lineNum += 1
	else:
		continue
        if len(line)>0 and line[0] == "#":
	    uid += 1
            keywords["headerfile"].append([lineNum,uid,line])
        else:
            tokens = line.split()
            if len(tokens)>0 and tokens[0] in dataTypes:
                if "(" and ")" in line:
		    uid += 1
                    keywords["function"].append([lineNum,uid,line])
                else:
                    variables = tokens[1].split(",")
                    for var in variables:
			uid += 1
                        keywords["variable"].append([lineNum,uid,var])
            else:
                if "(" and ")" in line:
		    uid += 1
                    keywords["function"].append([lineNum,uid,line])
                else:
		    uid += 1
                    keywords["operation"].append([lineNum,uid,line])

for key in keywords.keys():
	print(key+"--->")
	for token in keywords[key]:
		if len(token[2])>0 and token[2] != "," and token[2] != "''" and token[2] !="{" and token[2] != "}":
			print(token[0],token[1],re.sub(r'\s','',token[2]))
		else:
			uid += 1
			special.append(token)
	print("==============================================")
print("special--->")
for i in special:
	print(i[0],i[1],re.sub(r'\s','',i[2]))
