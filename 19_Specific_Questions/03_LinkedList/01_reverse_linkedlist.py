class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def addNode(self, head, newNode):
        self.currNode = head
        while self.currNode.next is not None:
            self.currNode = self.currNode.next
        self.currNode.next = newNode
        
    def printLinkedList(self, head):
        self.curr = head
        while self.curr is not None:
            print(self.curr.val)
            self.curr = self.curr.next
            

head = Node(1)

obj = LinkedList()
arr = [2,3,4,5,6]
for i in range(len(arr)):
    newNode = Node(arr[i])
    obj.addNode(head, newNode)
obj.printLinkedList(head)
    
# Reverse LinkedList
currNode = head
temp1 = None
while currNode is not None:
    if currNode == head:
        temp1 = currNode
        currNode = currNode.next
        temp1.next = None
    else:
        temp2 = currNode 
        currNode = currNode.next
        temp2.next = temp1
        temp1 = temp2
obj.printLinkedList(temp1)
        