precedence = {
    "y": 3,
    "u": 2.5,   # unary minus
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
    "$": 0
}

OPS = ["+", "-", "*", "/","u"]
 
operation = "y+y*yuy"  # "E+E-E/E*E"#  input("Enter the operation: ")
operation = operation + "$"


symbols = list(set(operation))
symbols.sort()

symbols = symbols[::-1]
idx = symbols[0]

print("OPERATIONS: ","".join(operation))
print()

OPT = [[]]

for i in symbols:
    temp = []
    for j in symbols:
        if i == j and (i == idx or i == "$"):
            temp.append("-")
        elif precedence[i] >= precedence[j]:
            temp.append(">")
        else:
            temp.append("<")

    OPT.append(temp)

OPT = OPT[1:]
print(" ", *symbols)
for i, op in enumerate(OPT):
    print(symbols[i], *op)


print("-" * 50)
print()


# Algorithm


STACK = ["$"]
current = 0

print("STACK: {stack} | INPUT: {oper} | Action: {act}".format(
    stack="".join(STACK), oper=operation[current:], act="INITIAL"))
while True:
    # a = stack top , b = point current
    a = STACK[-1]
    b = operation[current]

    if a == "$" and b == "$":
        print("STACK: {stack} | INPUT: {oper} | Action: {act}".format(
            stack="".join(STACK), oper=operation[current:], act="ACCEPT"))
        print("Found Terminal!")
        break

    pres = OPT[symbols.index(a)][symbols.index(b)]
    if pres == "<":
        STACK.append(b)
        current += 1
        print("STACK: {stack} | INPUT: {oper} | Action: {act}".format(
            stack="".join(STACK), oper=operation[current:], act="PUSH"))
    elif pres == ">":
        n_top = STACK.pop()
        print("STACK: {stack} | INPUT: {oper} | Action: {act}".format(
            stack="".join(STACK), oper=operation[current:], act="POP"))
        while OPT[symbols.index(STACK[-1])][symbols.index(n_top)] == ">":
            n_top = STACK.pop()

            print("STACK: {stack} | INPUT: {oper} | Action: {act}".format(
                stack="".join(STACK), oper=operation[current:], act="POP"))
    else:
        print("ERROR")

