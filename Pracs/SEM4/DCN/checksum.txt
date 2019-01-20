# ================= INPUT =====================
print("Enter data to be transmitted-")
data=input()
hexvals=[]

# ================= CONVERT TO HEX ============
for i in data:
  hexvals.append(hex(ord(i))[2:])
if len(hexvals)%2:
  hexvals.append('00')
# print("After converting ascii to hex-")
# print(*hexvals)

# ================= CONVERT TO 16 BIT HEX =====
bitvals=[]
for i in range(len(hexvals)//2):
  bitvals.append(hexvals[2*i]+hexvals[(2*i)+1])
# print("after making 16bit hex pairs-")
# print(*bitvals)

# ================= FIND HEX SUM ==============
hexsum=0
for i in range(len(bitvals)):
  hexsum+=int(bitvals[i],base=16)
hexsum=hex(hexsum)[2:]
print("Hexadecimal summation-")
print(hexsum)

# ================= FINDING COMPLEMENT ========
while len(hexsum)>4:  
  hexsum=hex(int(hexsum[len(hexsum)-4:],base=16)+int(hexsum[0:len(hexsum)-4],base=16))[2:]
while len(hexsum)<4:
  hexsum='0'+hexsum
final_transmitted=hexsum
print("Final sum, after wrapping, before complement-")
print(final_transmitted)
finallyans=[]
for i in range(len(final_transmitted)):
  finallyans.append(hex(int('f',base=16)-int(final_transmitted[i],base=16))[2:])
finallyans="".join(finallyans)
print("Sum after taking complement-")
print(finallyans)

# ================= RECEVIER PART ==============
print("Enter recevied data-")

data=input()
hexvals=[]

for i in data:
  hexvals.append(hex(ord(i))[2:])
if len(hexvals)%2:
  hexvals.append('00')
# print("After converting ascii to hex-")
# print(*hexvals)

eightbit_recvd=hexvals
sixteenbit_recvd=[]
for i in range(len(eightbit_recvd)//2):
  sixteenbit_recvd.append(eightbit_recvd[2*i]+eightbit_recvd[(2*i)+1])
# print("16 bit pairs of recveived data-")
# print(*sixteenbit_recvd)

# ================= FIND HEX SUM ==============
hexsum=0
for i in range(len(sixteenbit_recvd)):
  hexsum+=int(sixteenbit_recvd[i],base=16)
hexsum+=int(finallyans, base=16)
hexsum=hex(hexsum)[2:]
print("Hexadecimal summation-")
print(hexsum)

# ================= FINDING COMPLEMENT ========
while len(hexsum)>4:
  hexsum=hex(int(hexsum[len(hexsum)-4:],base=16)+int(hexsum[0:len(hexsum)-4],base=16))[2:]
while len(hexsum)<4:
  hexsum='0'+hexsum
final_recvd=hexsum
print("Final sum, after wrapping, before complement-")
print(final_recvd)
finallyrecvd=[]
for i in range(len(final_recvd)):
  finallyrecvd.append(hex(int('f',base=16)-int(final_recvd[i],base=16))[2:])
finallyrecvd="".join(finallyrecvd)
print("Sum after taking complement-")
print(finallyrecvd)



