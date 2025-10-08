import sys

n = int(input("Number of cities: "))
cities = [input(f"City {i+1}: ") for i in range(n)]
graph = [list(map(int, input(f"Distances from {cities[i]}: ").split())) for i in range(n)]
source = input("Source city: ")
dest = input("Destination city: ")
src, dst = cities.index(source), cities.index(dest)

dist = [sys.maxsize]*n; dist[src]=0
visited = [False]*n; parent = [-1]*n

for _ in range(n):
    u = min((d,i) for i,d in enumerate(dist) if not visited[i])[1]
    visited[u]=True
    for v in range(n):
        if graph[u][v]>0 and not visited[v] and dist[u]+graph[u][v]<dist[v]:
            dist[v]=dist[u]+graph[u][v]
            parent[v]=u

path=[]; i=dst
while i!=-1: path.append(cities[i]); i=parent[i]
path.reverse()

print(f"Shortest distance: {dist[dst]}")
print("Shortest path:", " -> ".join(path))
