print("Enter number of jobs")
jobs=int(input())
print("Enter profits for each job")
profits=list(map(int, input().split()))
print("Enter deadlines for each job")
deadlines=list(map(int, input().split()))
days=max(deadlines)
job_list=[0 for i in range(days)]
pairing=[]
for i in range(jobs):
	temp=[]
	temp.append(profits[i])
	temp.append(deadlines[i]-1)
	temp.append(i)
	pairing.append(temp)
pairing.sort(reverse=True)
days_allotted=[0 for i in range(jobs)]
for i in pairing:
	start=i[1]
	while(start>=0):
		if job_list[start]==0:
			job_list[start]=[i[0],i[2]]
			days_allotted[i[2]]=start+1			
			break
		else:
			start-=1
tot_prof=0
print("Jobs performed in order-")
for i in range(days):
	tot_prof+=job_list[i][0]	
	print(str(i+1)+". Job"+str(job_list[i][1]+1)+" "+str(job_list[i][0]))
print("Total profit")
print(tot_prof)
