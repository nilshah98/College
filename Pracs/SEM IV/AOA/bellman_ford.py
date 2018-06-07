MAX=100
print("Enter number of vertices in the graph")
v=int(input())
# print(v)
dist=[MAX for i in range(v+1)]
print("Enter source vertice")
src=int(input())
path=[[] for i in range(v+1)]
path[src].append(src)
# distance from a point to itself is 0
dist[src]=0
graph=[[MAX for i in range(v+1)] for j in range(v+1)]
#distance from self to self is 0
for i in range(v+1):
	# print(i)
	graph[i][i]=0
print("Enter the number of edges")
e=int(input())
for i in range(e):
	print("Enter "+str(i+1)+" edge, as src dest val format")
	s,d,val=map(int, input().split())
	graph[s][d]=val
print("Graph input:")
for i in range(1,v+1):
	# print(i)
	print(*graph[i][1:])
print("source is "+str(src))
print("Initial distance array-")
print(*dist[1:])
for i in range(1,v+1):
	print("distance array for "+str(i)+" iteration")
	print(*dist[1:])
	for j in range(1,v+1):
		if dist[j]>dist[i]+graph[i][j]:
			dist[j]=dist[i]+graph[i][j]
			path[j]=path[i][:]
			path[j].append(j)
# print("Final shortest path-")
# print(*dist[1:])
print("Paths are:")
for i in range(1,v+1):
	print("path for vertex "+str(i))
	print(*path[i])
	print("distance for vertex "+str(i))
	print(dist[i])