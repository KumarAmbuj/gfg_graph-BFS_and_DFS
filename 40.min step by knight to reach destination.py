class Pair:
    def __init__(self,x,y,l):
        self.x=x
        self.y=y
        self.l=l

def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def isvalid(x,y,vis,n):
    return x>=0 and x<=n and y>=0 and y<=n and vis[x][y]==False

def findminmoves(n,knightpos,targetpos):

    queue=Queue()
    vis=[[False for i in range(n+1)] for j in range(n+1)]

    vis[knightpos[0]][knightpos[1]]=True

    Enqueue(queue,Pair(knightpos[0],knightpos[1],0))

    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.x==targetpos[0] and rem.y==targetpos[1]:
            print(rem.l)
            break

        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]

        for k in range(8):
            x=rem.x+dx[k]
            y=rem.y+dy[k]

            if isvalid(x,y,vis,n):
                Enqueue(queue,Pair(x,y,rem.l+1))
                vis[x][y]=True




findminmoves(30,[1,1],[30,30])


