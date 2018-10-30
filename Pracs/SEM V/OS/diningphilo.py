import time
import threading

forks = [1,1,1,1,1]
room = 4

def waitRoom():
    global room
    if room == 0:
        return False
    else:
        room -= 1
        return True

def signalRoom():
    global room
    room += 1
    return True

def waitForks(i):
    global forks
    if forks[i] == 0:
        return False
    else:
        forks[i] -= 1
        return True

def signalForks(i):
    global forks
    forks[i] += 1
    print(*forks)
    return True


def diningphilo(x):
    global forks
    global room
    while(True):
        # think
        time.sleep(1)
        if(waitRoom()):
            if(waitForks(x%5)):
                if(waitForks((x+1)%5)):
                    # eat
                    print("Philosopher ",x," eating")
                    time.sleep(3)
                    signalForks((x+1)%5)
                    signalForks(x%5)
                    signalRoom()
                    print("Philosopher ",x," left room")

if __name__=="__main__":
    p1 = threading.Thread(target=diningphilo, args=(1,))
    p2 = threading.Thread(target=diningphilo, args=(2,))
    p3 = threading.Thread(target=diningphilo, args=(3,))
    p4 = threading.Thread(target=diningphilo, args=(4,))
    p5 = threading.Thread(target=diningphilo, args=(5,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    print("Done")