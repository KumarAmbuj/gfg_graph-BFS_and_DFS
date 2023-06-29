from collections import defaultdict
def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)


class Graph:
    def __init__(self):

        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):

        vis=[False for i in range(4)]

        queue=Queue()
        Enqueue(queue,s)

        while(Size(queue)):
            rem=Dequeue(queue)

            vis[rem]=True
            print(rem)

            for x in self.graph[rem]:
                if vis[x]==False:
                    Enqueue(queue,x)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(1)
