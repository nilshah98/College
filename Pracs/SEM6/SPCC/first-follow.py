'''
Grammar =>
S -> aBC | AD | cBD
A -> pD | Cc | ~
B -> bC | b
C -> e | fD | ~
D -> d
'''

grammar = {
"S" : ["aBC","AD","cBD"],
"A" : ["pD","Cc","~"],
"B" : ["bC","b"],
"C" : ["e","fD","~"],
"D" : ["d"]
}

nonTerm = ["S","A","B","C","D"]
Term = ["a","c","p","c","b","e","f","d"]

first = {}
follow = {}

def getFirst(sym):
    # If symbol is non terminal then find it's first
    if sym in nonTerm:
        # Check if first for the symbol has been already calculated
        if sym in first.keys():
            return first[sym][:]
        else:
            # Else, get the grammar for the said language
            gram = grammar[sym]
            frt = []
            # Loop through each expression and get their first
            for expr in gram:
                ind = 0
                val = getFirst(expr[ind])

                # while "~" is being found, go on removing it and checking next index
                while "~" in val:
                    val.remove("~")
                    ind += 1
                    if ind < len(expr):
                        val += getFirst(expr[ind])
                    else:
                        frt.append("~")

                frt += val
            first[sym] = list(set(frt[:]))
            return first[sym][:]
    else:
        return [sym][:]

for i in nonTerm:
    getFirst(i)

def getFollow(sym):
    flw = []
    for key in grammar.keys():
        for expr in grammar[key]:
            if sym in expr:
                ind = expr.index(sym)
                if ind+1 == len(expr):
                    flw += (getFollow(key))
                else:
                    frt = getFirst(expr[ind+1])
                    while "~" in frt:
                        frt.remove("~")
                        ind += 1
                        if ind+1 == len(expr):
                            frt += (getFollow(key))
                        elif ind < len(expr):
                            frt += (getFirst(expr[ind+1]))
                    flw += frt

    if sym == "S":
        flw.append("$")
    follow[sym] = list(set(flw))
    return follow[sym][:]

for i in nonTerm:
    getFollow(i)

for i in nonTerm:
    print("First: ", i , first[i])
    print("Follow: ", i ,follow[i])