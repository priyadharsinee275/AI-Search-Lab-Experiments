graph = {'S': [('A',2), ('B',1)],
         'A': [('G',10)],
         'B': [('G',4)],
         'G': []}
h = {'S': 4, 'A': 2, 'B': 3, 'G': 0}
true_cost = {'S': 5, 'A': 10, 'B': 4, 'G': 0}
for node in h:
    ok = "OK" if h[node] <= true_cost[node] else "VIOLATION"
    print(f"  h({node}) = {h[node]}   true = {true_cost[node]}   {ok}")
def astar(start, goal):
    queue = [(h[start], 0, [start])]
    while queue:
        queue.sort()
        f, g, path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path, g
        for n, w in graph[node]:
            queue.append((g + w + h[n],
                          g + w,
                          path + [n]))
path, cost = astar('S', 'G')
print("A* path :", path)
print("Cost    :", cost)