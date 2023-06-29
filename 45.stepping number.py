def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def findsteppingnumber(n,m):

    queue=Queue()

    for i in range(10):
        Enqueue(queue,str(i))

    while(Size(queue)):
        rem=Dequeue(queue)

        if int(rem)>=n and int(rem)<=m:
            print(rem)
        elif int(rem)>m:
            break

        if rem[-1]=='0':
            if len(rem)>1:
                Enqueue(queue, rem + '1')

        else:
            Enqueue(queue,rem+str(int(rem[-1])-1))
            Enqueue(queue, rem + str(int(rem[-1]) + 1))

findsteppingnumber(0,21)

print('****')
findsteppingnumber(10,15)



