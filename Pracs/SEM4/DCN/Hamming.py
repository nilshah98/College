import math
def totbits(n):
  data=n
  pair=0
  while(math.floor(math.log2(data+pair))+1!=pair):
    pair+=1
  return pair
print("Enter number of databits-")
nodatabits=int(input())
x=totbits(nodatabits)


print("Total number of bits in hammingcode-")
x=x+nodatabits
print(x)
print("Enter the databits-")
databits=list(input())
# if len(databits)<x:
#   for i in range(x-len(databits)-int(math.log2(x+1))):
#     databits.append("0")
databits=databits[::-1]
# print("".join(databits))
curr=0
hammingcode=[0 for i in range(x)]
# ====================
# GENERATING HAMMINGCODE
# ====================
for i in range(1,x+1):
  if math.log2(i)%1!=0:
    hammingcode[i-1]=databits[curr]
    curr+=1
# print(hammingcode)
nodatabits=len(databits)
# print(nodatabits)
for i in range(x-nodatabits):
  pairity=2**i
  currxor=0
  for j in range(1,x+1):
    if math.log2(j)%1!=0:
      if pairity&j:
        currxor^=int(hammingcode[j-1])
  hammingcode[pairity-1]=str(currxor)
hammingcode=hammingcode[::-1]
print("Hamming Code")
print("".join(hammingcode))

# ====================
# ERROR DETECTION
# ====================

print("Enter the code recvd for error detection-")
recvd=list(input())
# if len(recvd)<x:
#   for i in range(x-len(recvd)-int(math.log2(x+1))):
#     recvd.append("0")
recvdrev=recvd[::-1]

check=[0 for i in range(x-nodatabits)]
# print(check)
for i in range(len(check)):
  pairity=2**i
  currcheck=0
  for j in range(len(hammingcode)):
    if pairity&(j+1):
      currcheck^=int(recvdrev[j])
  check[i]=currcheck
place=0
for i in range(len(check)):
  if(check[i]):
    place+=2**i
check=check[::-1]
print("The syndrome is-")
print("".join(map(str,check)))
if place==0:
  print("No error")
else:
  loc=check[::-1].index(1)
  # print(check[::-1])
  print("Location " + str(2**loc) + " has error")