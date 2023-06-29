from collections import defaultdict

graph=defaultdict(list)

graph[1].append(2)
graph[1].append(4)
graph[2].append(4)
graph[3].append(9)

print(graph)