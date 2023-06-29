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
        self.graph=defaultdict(list)
        self.v=v

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,u,n):
        count=0
        vis=[False for i in range(self.v)]
        vis[u]=True
        queue=Queue()
        Enqueue(queue,[u,0])

        while(Size(queue)):

            rem=Dequeue(queue)

            if rem[1]==n:
                count+=1

            for v in self.graph[rem[u]]:
                if vis[v]==False:
                    vis[v]=True
                    Enqueue(queue,[v,rem[1]+1])

        print(count)

g=Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)

level = 2

g.bfs(0,level)



