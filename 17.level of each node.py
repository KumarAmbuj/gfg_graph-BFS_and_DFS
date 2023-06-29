def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)



from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,s):

        queue=Queue()
        vis=[False for i in range(self.v)]
        Enqueue(queue,[s,0])
        vis[s]=True

        while(Size(queue)):
            rem=Dequeue(queue)
            print(rem[0],rem[1])

            for v in self.graph[rem[0]]:
                if vis[v]==False:
                    vis[v]=True
                    Enqueue(queue,[v,rem[1]+1])


V = 8
g=Graph(V)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(1,5)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(6,7)
g.bfs(0)