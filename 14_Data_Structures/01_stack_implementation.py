stack = []
top = None

def isEmpty():
    if stack == []:
        return True
    else:
        return False

def push(element):
    global top
    stack.append(element)
    top = len(stack)-1
    
def pop():
    # del method stack.del(index)
    # remove method stack.remove(element)
    global top
    if(isEmpty()):
        print("Under Flow")
    else:
        x = stack.pop(top)
        top = top - 1
        print(x)
           
def peek():
    if(isEmpty()):
        print("Under Flow")
    else:
        global top
        print(stack[top])

def display():
    if(isEmpty()):
        print("Under flow")
    else:
        for items in stack:
            print(f"{items}")       
            
push(1)
push(2)
push(3)
push(4)
push(5)

print("Element at the peek: ")
peek()

print("Popping element")
pop()

print("Popping element")
pop()

display()


    