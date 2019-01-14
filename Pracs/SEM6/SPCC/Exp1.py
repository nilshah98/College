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
