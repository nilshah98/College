'''
Grammar =>
E -> T+F | T-F
T -> m*n | n
F -> a   | (E)

Extension =>
M -> m
N -> n
'''

def E(check,buf):
    buf = T(check,buf)
    if(check[buf] == "+"):
        buf += 1
        buf = F(check,buf)
    elif(check[buf] == "-"):
        buf += 1
        buf = F(check,buf)
    else:
        raise Exception("Invalid String")
    return buf

def T(check,buf):
    if(check[buf] == "m"):
        buf += 1
        if(check[buf] == "*"):
            buf += 1
            if(check[buf] == "n"):
                buf += 1
            else:
                raise Exception("Invalid String")
        else:
            raise Exception("Invalid String")
    elif(check[buf] == "n"):
        buf += 1
    else:
        raise Exception("Invalid String")
    return buf

def F(check,buf):
    if(check[buf] == "a"):
        buf += 1
    elif(check[buf] == "("):
        buf += 1
        buf = E(check,buf)
        if(check[buf] == ")"):
            buf += 1
        else:
            raise Exception("Invalid String")
    else:
        raise Exception("Invalid String")
    return buf

print("Enter string to test")
exp = input()
buf = E(exp,0)
if(buf == len(exp)):
    print("Verified!")