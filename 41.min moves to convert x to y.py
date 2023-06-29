class Pair():
    def __init__(self,n,l):
        self.n=n
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


def findminmoves(x,y):

    queue=Queue()
    Enqueue(queue,Pair(x,0))
    while(Size(queue)):
        rem=Dequeue(queue)
        if rem.n==y:
            print(rem.l)
            break
        Enqueue(queue,Pair(rem.n*2,rem.l+1))
        Enqueue(queue,Pair(rem.n-1,rem.l+1))

findminmoves(4,7)


