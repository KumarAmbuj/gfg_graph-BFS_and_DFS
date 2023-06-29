def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def isvalid(x,y,n,arr,vis):
    return x>=0 and x<n and y>=0 and y<n and (arr[x][y]==3 or arr[x][y]==2) and vis[x][y]==False

def findmin(s,d,arr,n):
    queue=Queue()
    vis=[[False for j in range(n)] for i in range(n)]

    vis[s[0]][s[1]]=True
    Enqueue(queue,[s,0])

    while(Size(queue)):
        rem=Dequeue(queue)

        if rem[0][0]==d[0] and rem[0][1]==d[1]:
            
            print(rem[1])
            break

        dx=[-1,0,1,0]
        dy=[0,1,0,-1]

        for k in range(4):
            x=rem[0][0]+dx[k]
            y=rem[0][1]+dy[k]

            if isvalid(x,y,n,arr,vis):
                vis[x][y]=True

                Enqueue(queue,[[x,y],rem[1]+1])


def findminmoves(arr):
    n=len(arr)
    s=[0,0]
    d=[0,0]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                s[0]=i
                s[1]=j
            if arr[i][j]==2:
                d[0]=i
                d[1]=j

    findmin(s,d,arr,n)

N = 4
M = [[3 , 3 , 1 , 0 ],
     [3 , 0 , 3 , 3 ],
     [2 , 3 , 0 , 3 ],
     [0 , 3 , 3 , 3 ]]
findminmoves(M)