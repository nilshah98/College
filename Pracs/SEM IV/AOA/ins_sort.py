# import time
#Insertion Sort
import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')


# start_time=time.time()
tim=[]
bst=[]
wrt=[]
avg=[]
for n in range(10,101,10):
  tim.append(n)
  avgarr=[random.randint(1,100) for i in range(n)]
  bstarr=sorted(avgarr)
  wrtarr=sorted(avgarr)[::-1]
  # ========================= AVERAGE CASE ==================== #  
  c=0
  for i in range(1,n):
    c+=1
    key=avgarr[i]
    c+=1
    j=i-1
    c+=1
    while j>=0 and key<avgarr[j]:
      c+=1
      avgarr[j+1]=avgarr[j]
      c+=1
      j-=1
      c+=1
    c+=1 #checking condition
    avgarr[j+1]=key
    c+=1
  c+=1 #checking condition 
  avg.append(c)
  # ========================= BEST CASE ==================== #
  c=0
  for i in range(1,n):
    c+=1
    key=bstarr[i]
    c+=1
    j=i-1
    c+=1
    while j>=0 and key<bstarr[j]:
      c+=1
      bstarr[j+1]=bstarr[j]
      c+=1
      j-=1
      c+=1
    c+=1 #checking condition
    bstarr[j+1]=key
    c+=1
  c+=1 #checking condition 
  bst.append(c)
  # ======================== WORST CASE ===================== #
  c=0
  for i in range(1,n):
    c+=1
    key=wrtarr[i]
    c+=1
    j=i-1
    c+=1
    while j>=0 and key<wrtarr[j]:
      c+=1
      wrtarr[j+1]=wrtarr[j]
      c+=1
      j-=1
      c+=1
    c+=1 #checking condition
    wrtarr[j+1]=key
    c+=1
  c+=1 #checking condition 
  wrt.append(c)
# print(time.time()-start_time)

# ================== PLOTTING GRAPHS ================ #

plt.scatter(tim,wrt)
plt.plot(tim,wrt, label="worst time")
plt.scatter(tim,bst)
plt.plot(tim,bst, label="best time")
plt.scatter(tim,avg)
plt.plot(tim,avg, label="average time")

# ====================== LEGEND ====================== #

plt.legend()

# ============= printing cordinates too ============== #

# for i in range(len(tim)):
#     plt.text(tim[i],avg[i],str(tim[i])+","+str(avg[i]))
# for i in range(len(tim)):
#     plt.text(tim[i],bst[i],str(tim[i])+","+str(bst[i]))
# for i in range(len(tim)):
#     plt.text(tim[i],wrt[i],str(tim[i])+","+str(wrt[i]))

plt.xlabel('test cases')
plt.ylabel('number of steps')
plt.title('insertion sort time complexity')
plt.savefig('ins_sort.png')
