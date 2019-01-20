import bisect

#FCFS
def FCFS(curr,tracks):
    cur = curr
    tot = 0
    seq = []
    for i in tracks:
        tot += abs(i - cur)
        seq.append(i)
        cur = i
    print("Avg disc access for FCFS- ",tot/len(tracks))
    print("Sequence of disc access- ",*seq)

#SSTF
def SSTF(curr,tracks):
    tracks.sort()
    cur = curr
    tot = 0
    seq = []
    mini = 10**7
    done = 0
    cpyt = tracks[:]
    while done < len(tracks):
        idx = bisect.bisect(cpyt,cur)
        if abs(cur - cpyt[(idx)%len(cpyt)]) <= abs(cur - cpyt[(idx-1)%len(cpyt)]):
            tot += abs(cur - cpyt[(idx)%len(cpyt)])
            seq.append(cpyt[(idx)%len(cpyt)])
            cur = cpyt[(idx)%len(cpyt)]
            del cpyt[(idx)%len(cpyt)]
        else:
            tot += abs(cur - cpyt[(idx-1)%len(cpyt)])
            seq.append(cpyt[(idx-1)%len(cpyt)])
            cur = cpyt[(idx-1)%len(cpyt)]
            del cpyt[(idx-1)%len(cpyt)]
        done += 1
    print("Avg disc access for SSTF- ",tot/len(tracks))
    print("Sequence of disc access- ",*seq)


#SCAN
def SCAN(curr,tracks):
    tracks.sort()
    cur = curr
    tot = 0
    seq = []
    idx = bisect.bisect(tracks,cur)
    cpy = idx
    n = len(tracks)
    done = 0
    forw = True
    while done < n:
        if idx == n:
            idx = cpy
            forw = False
        idx = idx%n
        tot += abs(cur - tracks[idx])
        seq.append(tracks[idx])
        cur = tracks[idx]
        done += 1
        if forw:
            idx += 1
        else:
            idx -= 1
    print("Avg disc access for SCAN- ",tot/n)
    print("Sequence of disc access- ",*seq)

#CSCAN
def CSCAN(curr,tracks):
    tracks.sort()
    cur = curr
    tot = 0
    seq = []
    idx = bisect.bisect(tracks,cur)
    cpy = idx
    n = len(tracks)
    done = 0
    while done < n:
        idx = idx%n
        tot += abs(cur - tracks[idx])
        seq.append(tracks[idx])
        cur = tracks[idx]
        idx += 1
        done += 1
    print("Avg disc access for CSCAN- ",tot/n)
    print("Sequence of disc access- ",*seq)

#LOOK
def LOOK(curr,tracks,maxi):
    tracks.sort()
    cur = curr
    tot = 0
    seq = []
    idx = bisect.bisect(tracks,cur)
    cpy = idx
    n = len(tracks)
    done = 0
    forw = True
    while done < n:
        if idx == n:
            idx = cpy
            forw = False
        idx = idx%n
        tot += abs(cur - tracks[idx])
        seq.append(tracks[idx])
        cur = tracks[idx]
        done += 1
        if forw:
            idx += 1
        else:
            idx -= 1
    tot += 2*(maxi - tracks[-1])
    print("Avg disc access for LOOK- ",tot/n)
    print("Sequence of disc access- ",*seq)


print("Enter the number of disk access")
n = int(input())
print("Enter current track head location")
curr = int(input())
print("Enter max number of tracks")
maximum = int(input())
print("Enter space separated disk access location")
tracks = list(map(int, input().split()))

FCFS(curr,tracks)
SSTF(curr,tracks)
SCAN(curr,tracks)
CSCAN(curr,tracks)
LOOK(curr,tracks,maximum)

