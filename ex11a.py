n = int(input("Enter number of users: "))
users = [input(f"Enter name of user {i+1}: ") for i in range(n)]

adj_matrix = [[0]*n for _ in range(n)]
adj_list = {user: [] for user in users}

m = int(input("Enter number of connections: "))
for _ in range(m):
    u1, u2 = input("Enter connection (user1 user2): ").split()
    i, j = users.index(u1), users.index(u2)
    adj_matrix[i][j] = adj_matrix[j][i] = 1
    adj_list[u1].append(u2)
    adj_list[u2].append(u1)

print("\nAdjacency List:")
for u in adj_list:
    print(u, "->", adj_list[u])

print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(row)

u1, u2 = input("\nCheck connection between (user1 user2): ").split()
i, j = users.index(u1), users.index(u2)

print("\nUsing Adjacency List:", "Connected" if u2 in adj_list[u1] else "Not Connected")
print("Using Adjacency Matrix:", "Connected" if adj_matrix[i][j] == 1 else "Not Connected")
