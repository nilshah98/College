import time
import threading
import random

criticalSection = []
mutualExclusion = 1
checkSize = 0

def semSignal():
	global mutualExclusion
	mutualExclusion = 1
	return True

def semWait():
	global mutualExclusion
	if(mutualExclusion == 1):
		mutualExclusion = 0
		return True
	else:
		return False

def semWaitB():
	global checkSize
	if(checkSize > 0):
		checkSize -= 1
		return True
	else:
		return False

def semSignalB():
	global checkSize
	checkSize += 1
	return True
	
def producer():
	global checkSize
	global sizeCriticalSection
	global criticalSection
	while(True):
		if(semWait()):
			checkSize += 1
			criticalSection.append(random.randint(1,10))
			print(checkSize)
			print(*criticalSection)
			semSignal()
			print("Producer")
			time.sleep(1)

def consumer():
	global checkSize
	global sizeCriticalSection
	global criticalSection
	while(True):
		if(semWaitB()):
			if(semWait()):
				checkSize -= 1
				print(criticalSection.pop())
				semSignal()
				print("Consumer")
				time.sleep(3)

if __name__=="__main__":
	t1 = threading.Thread(target=producer)
	t2 = threading.Thread(target=consumer)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Done")
