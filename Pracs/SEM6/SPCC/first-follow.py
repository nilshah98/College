'''
Grammar =>

S -> aBC | AD | cBD
A -> pD | Cc | ~
B -> bC | b
C -> e | fD | ~
D -> d
'''

grammar = {
"S" : ["aFC","AD","cFD"],
"A" : ["pD","Cc","~"],
"F" : ["bC","b"],
"C" : ["e","fD","~"],
"D" : ["d"]
}

nonTerm = ["S","A","F","C","D"]
Term = ["a","c","p","c","b","e","f","d"]

first = {}
follow = {}

def getFirst(sym):
    if sym in nonTerm:
        if sym in first.keys():
            return first[sym]
        else:
            gram = grammar[sym]
            frt = []
            for expr in gram:
                ind = 0
                val = getFirst(expr[ind])
                for i in val:
                    if i == "~":
                        ind += 1
                        if ind < len(expr):
                            val = getFirst(expr[ind])
                    else:
                        frt.append(i)
            first[sym] = list(set(frt))
            return first[sym]
    else:
        return [sym]

for i in nonTerm:
    getFirst(i)

def getFollow(sym):
    if sym == "S":
        follow[sym] = ["$"]
        return follow[sym]
    for key in grammar.keys():
        for expr in grammar[key]:
            if sym in expr:
                ind = expr.index(sym)
                if ind+1 == len(expr):
                    if sym in follow.keys():
                        for i in getFollow(key):
                            follow[sym].append(i)
                    else:
                        follow[sym] = getFollow(key)[:]
                else:
                    if sym in follow.keys():
                        if expr[ind+1] in nonTerm:
                            for i in first[expr[ind+1]]:
                                follow[sym].append(i)
                        else:
                            follow[sym].append(expr[ind+1])
                    else:
                        if expr[ind+1] in nonTerm:
                            follow[sym] = first[expr[ind+1]][:]
                        else:
                            follow[sym] = [expr[ind+1]]
    follow[sym] = list(set(follow[sym]))
    return follow[sym]

for i in nonTerm:
    getFollow(i)

for i in nonTerm:
    print(i,"====>")
    print("First: ", first[i])
    print("Follow: ",follow[i])