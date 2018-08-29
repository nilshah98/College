def final(process, queue, service, arrival):
	start = []
	end = []
	offset = len(queue)
	turn = 0
	wait = 0
	avgTurn = 0
	for i in range(1,process+1):
		start.append(queue.index(i))
		end.append(offset - queue[::-1].index(i))
	for i in range(process):
		print("Turnaround time for ",i+1," is")
		turn += end[i] - arrival[i]
		print(end[i] - arrival[i])
		print("Waiting time for ",i+1," is")
		wait += end[i] - arrival[i] - service[i]
		print(end[i] - arrival[i] - service[i])
		print("Normalised turnaround time for  ", i+1, " is")
		avgTurn += (end[i] - arrival[i])/service[i]
		print((end[i] - arrival[i])/service[i])
	print("Average turnaround time-")
	print(turn/process)
	print("Average waiting time-")
	print(wait/process)
	print("Average normalised turnaround time- ")
	print(avgTurn/process)


print("Enter the number of process")
numProcesses = int(input())
process = [ i for i in range(1,numProcesses+1) ]
arrivalTime = []
serviceTime = []
queue = []
for i in range(numProcesses):
	print("Enter arrival time for ",i+1," process")
	arrivalTime.append(int(input()))
	print("Enter service time for ",i+1," process")
	serviceTime.append(int(input()))

# FCFS
currTime = 0
flag = True
asp = list(zip(arrivalTime, serviceTime, process))
asp.sort()
currIndex = 0
while flag:
	if currTime >= asp[currIndex][0]:
		for i in range(asp[currIndex][1]):
			queue.append(asp[currIndex][2])
		currTime += asp[currIndex][1]
		currIndex += 1
	else:
		currTime += 1
		queue.append(0)
	if currIndex >= numProcesses:
		flag = False
print("FCFS non-preemptive - ")
print(*queue)
final(numProcesses, queue, serviceTime, arrivalTime)



# SJF
currIndex = 1
sfjQueue = []
currTime = 0
flag = True
sap = list(zip(serviceTime, arrivalTime, process))
while flag:
	poss = []
	for i in sap:
		if currTime >= i[1]:
			poss.append(i)
	poss.sort()

	if len(poss)>0:
		job = poss[0]
		index = sap.index(job)
		for i in range(job[0]):
			sfjQueue.append(job[2])
		del sap[index]
		currIndex += 1
		currTime += job[0]
	else:
		sfjQueue.append(0)

	if len(sap) <= 0:
		flag = False
print("SFJ non-preemptive - ")
print(*sfjQueue)
final(numProcesses, sfjQueue, serviceTime, arrivalTime)


# Priority
currIndex = 1
priority = []
for i in range(numProcesses):
	print("Enter priorty of ",i+1," job")
	priority.append(int(input()))
priorityQueue = []
currTime = 0
flag = True
psap = list(zip(priority ,serviceTime, arrivalTime, process))
while flag:
	poss = []
	for i in psap:
		if currTime >= i[2]:
			poss.append(i)
	poss.sort()

	if len(poss)>0:
		job = poss[0]
		index = psap.index(job)
		for i in range(job[1]):
			priorityQueue.append(job[3])
		del psap[index]
		currIndex += 1
		currTime += job[1]
	else:
		priorityQueue.append(0)

	if len(psap) <= 0:
		flag = False

print("Priority non-preemptive - ")
print(*priorityQueue)
final(numProcesses, priorityQueue, serviceTime, arrivalTime)



print("Enter the time slice for the processor")
timeSlice = int(input())


