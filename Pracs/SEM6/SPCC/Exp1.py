#=================TOKENS================================
keywords = {
"variable":[],
"headerfile":[],
"function":[],
"operation":[]
}

dataTypes = ["int","char","float","bool","void"]
operators = ["=","+","-","*","/"]
#=================READ C FILE=========================== 
f = open("./hello.c")
program = f.read()
f.close

#=================SPLIT BY LINE=========================
programLines = program.split(";")
for line in programLines:
    newLines = line.split("\n")
    for line in newLines:
        if len(line)>0 and line[0] == "#":
            keywords["headerfile"].append(line)
        else:
            tokens = line.split()
            if len(tokens)>0 and tokens[0] in dataTypes:
                if "(" and ")" in line:
                    keywords["function"].append(line)
                else:
                    variables = tokens[1].split(",")
                    for var in variables:
                        keywords["variable"].append(var)
            else:
                if "(" and ")" in line:
                    keywords["function"].append(line)
                else:
                    keywords["operation"].append(line)

print(keywords)