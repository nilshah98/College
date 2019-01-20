# import time
#Selection Sort
import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


plt.style.use('ggplot')

tim=[]
bst=[]
avg=[]
wrt=[]
for n in range(10,101,10):
  tim.append(n)
  # start_time=time.time()
  avgarr=[random.randint(1,100) for i in range(n)]
  bstarr=sorted(avgarr)
  wrtarr=sorted(avgarr)[::-1]
  # ========================= AVERAGE CASE ==================== #  
  c=0
  for i in range(len(avgarr)):
    c+=1
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    c+=1
    for j in range(i+1, len(avgarr)):
      c+=1
      if avgarr[min_idx] > avgarr[j]:
        c+=1
        min_idx = j
        c+=1
      c+=1 #checking condition
    c+=1 #checking condition
    # Swap the found minimum element with 
    # the first element        
    avgarr[i], avgarr[min_idx] = avgarr[min_idx], avgarr[i]
    c+=1
  c+=1 #checking condition
  avg.append(c)
  # ========================= BEST CASE ==================== #  
  c=0
  for i in range(len(bstarr)):
    c+=1
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    c+=1
    for j in range(i+1, len(bstarr)):
      c+=1
      if bstarr[min_idx] > bstarr[j]:
        c+=1
        min_idx = j
        c+=1
      c+=1 #checking condition
    c+=1 #checking condition
    # Swap the found minimum element with 
    # the first element        
    bstarr[i], bstarr[min_idx] = bstarr[min_idx], bstarr[i]
    c+=1
  c+=1 #checking condition
  bst.append(c)
  # ========================= WORST CASE ==================== #
  c=0
  for i in range(len(wrtarr)):
    c+=1
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    c+=1
    for j in range(i+1, len(wrtarr)):
      c+=1
      if wrtarr[min_idx] > wrtarr[j]:
        c+=1
        min_idx = j
        c+=1
      c+=1 #checking condition
    c+=1 #checking condition
    # Swap the found minimum element with 
    # the first element        
    wrtarr[i], wrtarr[min_idx] = wrtarr[min_idx], wrtarr[i]
    c+=1
  c+=1 #checking condition
  wrt.append(c)
  # print(time.time() - start_time)


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
plt.title('selection sort time complexity')
plt.savefig('sel_sort.png')
