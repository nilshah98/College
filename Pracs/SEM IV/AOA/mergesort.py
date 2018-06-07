# import time
#Merge Sort
import random
import math
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')


# =============== MERGE SORT =================== #

# ================ MERGING ==================== # 

def merge(arr, l, m, r, c):
    n1 = m - l + 1
    n2 = r- m
    c+=2
    # create temp arrays
    
    L = [0] * (n1)
    c+=n1
    
    R = [0] * (n2)
    c+=n2

    
    # Copy data to temp arrays L[] and R[]
    
    for i in range(0 , n1):
        c+=1
        L[i] = arr[l + i]
        c+=1
    c+=1
    
    for j in range(0 , n2):
        c+=1
        R[j] = arr[m + 1 + j]
        c+=1
    c+=1

    L.append(math.inf)
    R.append(math.inf)
    print(L,"left")
    print(R,"right")
    c+=2
    
    
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    c+=2
    
    # print(arr)
    # print(l,r+1,"range")
    for k in range(l,r+1):
        c+=1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            c+=2
        else:
            arr[k] = R[j]
            j += 1
            c+=2
        c+=1
    c+=1
    # print(arr)
    # Copy the remaining elements of L[], if there
    # are any
    
    return c
 
# ===================== SPLITTING ==================== #

def mergeSort(arr,l,r,c):
    # print(l,r)
    if l < r:
        c+=1

        m = (l+r)//2
        # print(m)
        c+=1
        # Sort first and second halves
        c+=1
        mergeSort(arr, l, m,c)
        c+=1
        mergeSort(arr, m+1, r,c)
        c+=1
        c+=merge(arr, l, m, r,c)
    c+=1
    return c

# =============== DRIVER PROGRAM =================== #

tim=[]
bst=[]
avg=[]
wrt=[]
arr=[38,27,45,6,3]
c=0
mergeSort(arr,0,4,c)
# for n in range(10,101,1):
#   tim.append(n)
#   # start_time=time.time()
#   avgarr=[random.randint(1,100) for i in range(n)]
#   bstarr=sorted(avgarr)
#   wrtarr=sorted(avgarr)[::-1]
#   # ========================= AVERAGE CASE ==================== #  
#   c=0
#   # print(avgarr)
#   c=mergeSort(avgarr,0,n-1,c)
#   # print(avgarr)
#   avg.append(c)
#   # ========================= BEST CASE ==================== #  
#   c=0
#   c=mergeSort(bstarr,0,n-1,c)
#   bst.append(c)
#   # ========================= WORST CASE ==================== #
#   c=0
#   c=mergeSort(wrtarr,0,n-1,c)
#   wrt.append(c)
#   # print(time.time() - start_time)


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
plt.title('merge sort time complexity')
plt.figure(2)
plt.xlabel('test cases')
plt.ylabel('number of steps')
plt.title('merge sort time complexity')
plt.figure(3)
plt.xlabel('test cases')
plt.ylabel('number of steps')
plt.title('merge sort time complexity')

plt.figure(1)
plt.savefig('merge_sort_wrt.png')
plt.figure(2)
plt.savefig('merge_sort_bst.png')
plt.figure(3)
plt.savefig('merge_sort_avg.png')