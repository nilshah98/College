import time
import threading
import random
import datetime

criticalSection = 0
readcount = 0 

readcountSem = 1
writeSem = 1 

testF = open("test.txt","w+")

def semSignalX():
	global writeSem 
	writeSem = 1
	return True

def semWaitX():
	global readcountSem 
	if(readcountSem == 1):
		readcounrSem = 0
		return True
	else:
		return False

def semWaitR():
	global readcountSem
	if(readcountSem == 1):
		readcountSem == 0
		return True
	else:
		return False

def semSignalR():
	global readcountSem
	readcountSem = 1
	return True
	
def reader():
	global testF
	global readcountSem
	global writeSem
	global readcount
	global criticalSection
	while(True):
		if(semWaitR()):
			readcount += 1
			if(readcount == 1):
				if(semWaitX()):	
					print("Readers:", readcount)
					semSignalR()
					testF = open("test.txt","r")
					val = testF.read()
					print("Reading: ",val)
					if(semWaitR()):
						readcount -= 1
						if(readcount == 0):
							semSignalX()
						semSignalR()
					time.sleep(1)
			elif(readcount > 1):
				print("Readers:", readcount)
				semSignalR()
				testF = open("test.txt","r")
				val = testF.read()
				print("Reading: ",val)
				if(semWaitR()):
					readcount -= 1
					if(readcount == 0):
						semSignalX()
					semSignalR()
				time.sleep(1)

def writer():
	global testF
	global readcountSem
	global writeSem
	global readcount
	global criticalSection
	while(True):
		if(semWaitX()):
			val = str(datetime.datetime.now())
			testF = open("test.txt","w")
			testF.write(val)
			print("Writer: ",val)
			semSignalX()
			time.sleep(3)

if __name__=="__main__":
	r1 = threading.Thread(target=reader)
	r2 = threading.Thread(target=reader)
	w1 = threading.Thread(target=writer)

	r1.start()
	r2.start()
	w1.start()

	r1.join()
	r2.join()
	w1.join()
	print("Done")
