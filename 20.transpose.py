from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def printgraph(self):

        for x in self.graph:

            print('[{}]'.format(x),end='')
            for v in self.graph[x]:
                print('->{}'.format(v),end='')
            print()

    def findtranspose(self):

        print('r')
        g=Graph(self.v)

        for x in self.graph:
            for v in self.graph[x]:
                g.addEdge(v,x)

        for x in g.graph:

            print('[{}]'.format(x), end='')
            for v in g.graph[x]:
                print('->{}'.format(v), end='')
            print()


v = 5
g=Graph(v)
g.addEdge( 0, 1)
g.addEdge( 0, 4)
g.addEdge( 0, 3)
g.addEdge( 2, 0)
g.addEdge( 3, 2)
g.addEdge( 4, 1)
g.addEdge( 4, 3)
g.printgraph()
g.findtranspose()


