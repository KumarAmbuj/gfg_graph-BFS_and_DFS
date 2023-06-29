from collections import defaultdict
def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,u,vis,l):

        queue=Queue()


        vis[u]=True
        Enqueue(queue,u)
        while(Size(queue)):
            u=Dequeue(queue)
            l.append(u)

            for v in self.graph[u]:
                if vis[v]==False:
                    vis[v]=True
                    Enqueue(queue,v)

    def findbfs(self):

        vis=[False for i in range(self.v)]
        for i in range(self.v):
            if vis[i]==False:

                l=[]
                self.bfs(i,vis,l)
                print(*l)


V = 5
g=Graph(V)
g.addEdge(0, 4)
g.addEdge( 1, 2)
g.addEdge( 1, 3)
g.addEdge( 1, 4)
g.addEdge( 2, 3)
g.addEdge( 3, 4)
g.findbfs()
