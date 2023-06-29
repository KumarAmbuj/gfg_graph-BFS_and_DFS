

def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def findsmallestbinaryno(n):

    s='1'

    queue=Queue()
    Enqueue(queue,s)

    while(Size(queue)):

        rem=Dequeue(queue)

        if int(rem)%n==0:
            print(rem)
            break

        Enqueue(queue,rem+'0')
        Enqueue(queue,rem+'1')

findsmallestbinaryno(17)
