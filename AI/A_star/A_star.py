#This code looks ERRATIC, printing wrong OUTPUT, in the terminal. VERY DISRESPECTFUL!!

nodes_num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
dist_from_A = [10000,10000,10000,10000,10000,10000]
visited = [0,0,0,0,0,0]
path = []

graph = [
    [0, 7, 8, 9, 0, 0],
    [7, 0, 11, 0, 0, 20],
    [8, 11, 0, 0, 4, 12],
    [9, 0, 0, 0, 18, 0],
    [0, 0, 4, 18, 0, 6],
    [0, 20, 12, 0, 6, 0]
]

heuristic = [30, 100, 110, 80, 70, 50]

def route_traverse(node):
    global dist_from_A
    global graph
    global nodes_num
    global path
    global visited

    if node == 'F':
        path.append(node)
        return path

    cost = float('inf')
    next_node = None

    for i in range(len(graph[nodes_num[node]])):
        if graph[nodes_num[node]][i] != 0 and visited[i] == 0:
            total_cost = heuristic[i] + dist_from_A[nodes_num[node]] + graph[nodes_num[node]][i]
            print(graph[nodes_num[node]][i])
            if total_cost < cost:
                cost = total_cost
                next_node = list(nodes_num.keys())[i]
                print(next_node)

    if next_node:
        dist_from_A[nodes_num[next_node]] = cost
        visited[nodes_num[next_node]] = 1
        path.append(next_node)
        return route_traverse(next_node)

    return path

path = route_traverse('A')
print(path)