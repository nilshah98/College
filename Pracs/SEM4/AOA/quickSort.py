import random
import math
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')


def partition(arr,l,r,c):
  pivot=arr[l]
  lo=l+1
  hi=r
  c[0]+=3
  while(lo<=hi):
    c[0]+=1
    # print (A)
    while(arr[hi]>pivot):
      hi=hi-1
      c[0]+=2
    while(lo<=hi and arr[lo]<pivot):
      lo=lo+1
      c[0]+=2
    if (lo<hi):
      temp=arr[lo]
      arr[lo]=arr[hi]
      arr[hi]=temp
      c[0]+=4
      
  temp=arr[l]
  arr[l]=arr[hi]
  arr[hi]=temp
  c[0]+=3
  return [hi,c]

def quickSort(arr,l,r,c):

  if (l<r):
    c[0]+=1
    q=partition(arr,l,r,c)
    quickSort(arr,l,q[0]-1,q[1])
    quickSort(arr,q[0]+1,r,q[1])
  if(l==0 and r==len(arr)-1):
    return (c[0])
# A=[12,85,96,74,23]
# x=quickSort(A,0,len(A)-1,[0])
# print(x)
# =========================== GRAPH PART ======================
tim=[]
bst=[]
avg=[]
wrt=[]
c=0
for n in range(10,15,1):
  tim.append(n)
  # start_time=time.time()
  avgarr=[random.randint(1,100) for i in range(n)]
  bstarr=sorted(avgarr)
  wrtarr=sorted(avgarr)[::-1]
  # ========================= AVERAGE CASE ==================== #  
  c=[0]
  # print(avgarr)
  c=quickSort(avgarr,0,n-1,c)
  # print(avgarr)
  avg.append(c)
  # ========================= BEST CASE ==================== #  
  c=[0]
  c=quickSort(bstarr,0,n-1,c)
  bst.append(c)
  # ========================= WORST CASE ==================== #
  c=[0]
  c=quickSort(wrtarr,0,n-1,c)
  wrt.append(c)
  # print(time.time() - start_time)

print (bst)
print (avg)
print (wrt)
# ================== PLOTTING GRAPHS ================ #
plt.figure(1)
plt.scatter(tim,wrt)
plt.plot(tim,wrt, label="worst time")
plt.figure(2)
plt.scatter(tim,bst)
plt.plot(tim,bst, label="best time")
plt.figure(3)
plt.scatter(tim,avg)
plt.plot(tim,avg, label="average time")

# ====================== LEGEND ====================== #

plt.figure(1)
plt.legend()
plt.figure(2)
plt.legend()
plt.figure(3)
plt.legend()

# ============= printing cordinates too ============== #

# for i in range(len(tim)):
#     plt.text(tim[i],avg[i],str(tim[i])+","+str(avg[i]))
# for i in range(len(tim)):
#     plt.text(tim[i],bst[i],str(tim[i])+","+str(bst[i]))
# for i in range(len(tim)):
#     plt.text(tim[i],wrt[i],str(tim[i])+","+str(wrt[i]))
plt.figure(1)
plt.xlabel('test cases')
plt.ylabel('number of steps')
plt.title('quick sort time complexity')
plt.figure(2)
plt.xlabel('test cases')
plt.ylabel('number of steps')
plt.title('quick sort time complexity')
plt.figure(3)
plt.xlabel('test cases')
plt.ylabel('number of steps')
plt.title('quick sort time complexity')

plt.figure(1)
plt.savefig('quick_sort_wrt.png')
plt.figure(2)
plt.savefig('quick_sort_bst.png')
plt.figure(3)
plt.savefig('quick_sort_avg.png')