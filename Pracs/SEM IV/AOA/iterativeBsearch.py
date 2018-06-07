import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import random
import time

plt.style.use('ggplot')

def binarySearch(arr, l, r, x, c):
    c+=1
    while l <= r:
        c+=1
        mid = l + (r - l)//2;
         
        if arr[mid] == x:
            c+=1
            return c
 
        elif arr[mid] < x:
            c+=1
            l = mid + 1
 
        else:
            c+=1
            r = mid - 1
  
    return c
avgcase=[]
bstcase=[]
wrtcase=[]
avgtime=[]
bsttime=[]
wrttime=[]
times=[]
for i in range(10,101,10):
  times.append(i)
  arr=[j for j in range(i)]
  search=arr[random.randint(0,i-1)]
  avg_start_time=time.time()
  avgcount=binarySearch(arr,0,i-1,search,0)
  avg_fin_time=avg_start_time-time.time()
  avg_fin_time*=-1
  avgtime.append(avg_fin_time)
  
  bst_start_time=time.time()
  bstcount=binarySearch(arr,0,i-1,arr[(i-1)//2],0)
  bst_fin_time=bst_start_time-time.time()
  bst_fin_time*=-1
  bsttime.append(bst_fin_time)
  
  wrt_start_time=time.time()
  wrtcount=binarySearch(arr,0,i-1,i,0)
  wrt_fin_time=wrt_start_time-time.time()
  wrt_fin_time*=-1
  wrttime.append(wrt_fin_time)
  
  bstcase.append(bstcount)
  avgcase.append(avgcount)
  wrtcase.append(wrtcount)
plt.plot(times,avgcase,label="average case")
plt.scatter(times,avgcase)
plt.plot(times,bstcase,label="best case")
plt.scatter(times,bstcase)
plt.plot(times,wrtcase,label="worst case")
plt.scatter(times,wrtcase)

plt.legend()

plt.xlabel('test cases')
plt.ylabel('number of steps')

plt.savefig('binary_search.png')
  
# ============= SPACE COMPLEXITY ==============
# Space Complexity of an algorithm is total space taken by the algorithm with respect to the input size. Space complexity includes both Auxiliary space and space used by input.

# So, the space complexity here, is again summation of all the memory used, all the variables, arrays and function calls. As there is an array of size n here, others can be ignored, as they are comparable or smaller than the size n.

# So, the space complexity is O(n).

# If, you conside auxillary space complexity, which is the extra space or temporary space used by an algorithm, then it is O(1) here, as it uses only temporary variables, mid, ub, lb, and searchelem.