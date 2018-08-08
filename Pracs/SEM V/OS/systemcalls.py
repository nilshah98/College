import os
def parent_child():
	syscall = os.open('syscall.txt',os.O_RDWR)
	n = os.fork()
	if n>0:
		print os.read(syscall,100)
		os.write(syscall,'from parent process')
		print("Parent process")
		print("Parent process id is: ", os.getpid())
		print("Child process id is: ", n)
		status = os.wait()
		print(status)
		print("Child exit code: ", os.WEXITSTATUS(status[1]))
	elif n==0:
		print os.read(syscall,100)
		os.write(syscall,'from child  process')
		print("Child process")
		print("Parent process id is: ", os.getppid())
		print("Child process id is: ", os.getpid())
parent_child()
