import math
# TAKING INPUT HERE
print("Enter valid IPv4 address")
ip = list(map(int,input().split(".")))
print("Enter number of blocks to divide network into")
n_blocks = int(input())

# FINDING CLOSEST POWER OF 2 TO GET BLOCKS
if math.log(n_blocks,2)%1:
    n_hostbits = int(math.log(n_blocks,2)) + 1
else:
    n_hostbits = int(math.log(n_blocks,2))
n_blocks = 2**(n_hostbits)

# FINDING CLASS OF THE ADDRESS
if ip[0] <= 127:
    #CLASS A
    hostbits = 32
    if n_hostbits > hostbits:
        print("Too many subnets!")
    else:
        networkmask = [255]
        for i in range(n_hostbits//8):
            networkmask.append(255)
        fin = 0
        for i in range(n_hostbits%8):
            fin += 2**(7-i)
        networkmask.append(fin)
        while len(networkmask) < 4:
            networkmask.append(0)
elif ip[0] <= 191:
    #CLASS B
    hostbits = 16
    if n_hostbits > hostbits:
        print("Too many subnets!")
    else:
        networkmask = [255,255]
        for i in range(n_hostbits//8):
            networkmask.append(255)
        fin = 0
        for i in range(n_hostbits%8):
            fin += 2**(7-i)
        networkmask.append(fin)
        while len(networkmask) < 4:
            networkmask.append(0)
elif ip[0] <= 223:
    #CLASS C
    hostbits = 8
    if n_hostbits > hostbits:
        print("Too many subnets!")
    else:
        networkmask = [255,255,255]
        for i in range(n_hostbits//8):
            networkmask.append(255)
        fin = 0
        for i in range(n_hostbits%8):
            fin += 2**(7-i)
        networkmask.append(fin)
        while len(networkmask) < 4:
            networkmask.append(0)
else:
    #CLASS D or E
    pass
    networkmask = [255,255,255,255]

print("Subnet mask is:")
print(".".join(map(str, networkmask)))
