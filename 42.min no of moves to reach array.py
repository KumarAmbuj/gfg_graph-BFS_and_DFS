class Pair:
    def __init__(self,index,level):
        self.index=index
        self.level=level

def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def findminmoves(arr):

    n=len(arr)
    queue=Queue()
    Enqueue(queue,Pair(0,0))
    vis=[False for i in range(n)]
    vis[0]=True
    while(Size(queue)):
        rem=Dequeue(queue)

        
        if rem.index==n-1:
            print(rem.level)
            break

        if rem.index>0 and vis[rem.index-1]==False:
            Enqueue(queue,Pair(rem.index-1,rem.level+1))
            vis[rem.index-1]=True
        if rem.index<=(n-2) and vis[rem.index+1]==False:
            Enqueue(queue,Pair(rem.index+1,rem.level+1))
            vis[rem.index+1]=True
        for i in range(rem.index+1,n):
            if arr[i]==arr[rem.index]:
                Enqueue(queue,Pair(i,rem.level+1))
                vis[i]=True


arr = [0, 1, 2, 3, 4, 5, 6, 7, 5, 4,
                 3, 6, 0, 1, 2, 3, 4, 5, 7]

findminmoves(arr)

arr = [ 5, 4, 2,  5, 0]

findminmoves(arr)
