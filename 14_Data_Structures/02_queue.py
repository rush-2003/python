#  Insertion Back
#  Removal Fron
#  FIFO
#  front, rear, enque(), dequeue(), peek()

queue = []
f = None
r = None

def isEmpty():
    if queue == []:
        return True
    else:
        return False
    
def enqueue(item):
    global f, r 
    queue.append(item)
    if len(queue) == 1:
        f = r = 0
    else:
        r = len(queue) - 1
        
def dequeue():
    global f, r
    if(isEmpty()):
        print("Underflow")
    else:
        i = queue.pop(0)
        print(i)
    if(len(queue) == 0):
        f = r = None
        
def peek():
    global f, r
    if(isEmpty()):
        print("Underflow")
    else:
        f = 0
        print(queue[f])
    
def display():
    if(isEmpty()):
        print("Underflow")
    if(len(queue) == 1):
        print(queue[0])
    else:
        print(queue)
        
        
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)

dequeue()
dequeue()

peek()

display()