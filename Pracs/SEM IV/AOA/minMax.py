# MIN MAX
def maxmin(i,j,maxi,mini,arr):
  if (i==j):
    maxi=arr[i]
    mini=arr[i]
    return maxi,mini
  
  elif(i==(j-1)):
    if(arr[i]<arr[j]):
      mini=arr[i]
      maxi=arr[j]
    else:
      mini=arr[j]
      maxi=arr[i]
    return maxi,mini
  
  else:
    mid=(i+j)//2
    maxi1,mini1 = maxmin(i,mid,maxi,mini,arr)
    maxi2,mini2 = maxmin(mid+1,j,maxi,mini,arr)
    
    if(maxi1>maxi2):
      maxi=maxi1
    else:
      maxi=maxi2
    
    if(mini1<mini2):
      mini=mini1
    else:
      mini=mini2
    
    return maxi,mini

A=[]
for i in range(1,101):
  A.append(i)
mini=10**7
maxi=0
print(maxmin(0,len(A)-1,maxi,mini,A))
