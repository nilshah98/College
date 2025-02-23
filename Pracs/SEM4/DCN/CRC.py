def division(divisor,dividend):
  while len(dividend)>=len(divisor):  
    if divisor[0]==dividend[0]:
      for i in range(len(divisor)):
        dividend[i]^=divisor[i]
    # SHIFTING
    dividend=dividend[1::]
  return dividend

# ====================
# AUGMENTED CODE
# ==================== 
print("Enter the number codeword length")
nobits=int(input())
print("Enter the length of data to be transmitted, ie. dataword")
datal=int(input())
print("Enter the data to be transmitted")
data=list(input())

if(len(data)>=nobits):
  print("No of data bits need to be more")
else:
  temp=len(data)
  for i in range(nobits-len(data)):
    data.append("0")
print("Enter Divisor")
divisor=list(input())
divisor=list(map(int, divisor))
data=list(map(int, data))
print(divisor)
print(data)
# print(len(divisor))
# print(len(data))
if(nobits-temp<len(divisor)-1):
  # since remainder can be at least of length, divisor-1
  print("Error")
else:
  dividend=division(divisor,data[::1])
  print(dividend)
  if len(dividend)<nobits-temp:
    for i in range(nobits-temp-len(dividend)):
      data[temp+i]=0
  for i in range(len(dividend)):
    data[temp+nobits-temp-len(dividend)+i]=dividend[i]
  
  print("Augmented Code")
  print("".join(map(str, data)))
  
# ====================
# ERROR DETECTION
# ====================
print("Enter the recieved message")
recvd=list(input())
if len(recvd)!=nobits:
  print("Recieved length not equal to transmitted length")
else:
  recvd=list(map(int, recvd))
  ans=division(divisor,recvd)
  if len(ans)<nobits-datal:
    for i in range(nobits-datal-len(ans)):
      ans.insert(0,0)
  print("Syndrome-")
  print("".join(map(str,ans)))