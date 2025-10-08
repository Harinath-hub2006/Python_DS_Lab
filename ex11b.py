def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set([start])
    queue = [start]  

    while queue:
        vertex = queue.pop(0)  
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


n = int(input("Enter number of nodes: "))
nodes = [input(f"Enter node {i+1}: ") for i in range(n)]

m = int(input("Enter number of edges: "))
graph = {node: [] for node in nodes}

for _ in range(m):
    u, v = input("Enter edge (node1 node2): ").split()
    graph[u].append(v)
    graph[v].append(u)  

start_node = input("Enter starting node: ")
print("DFS traversal starting at node", start_node, ":")
dfs(graph, start_node)
print("\nBFS traversal starting at node", start_node, ":")
bfs(graph, start_node)

