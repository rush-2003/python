# create Nodes
# create linkedlist
# add nodes to linkedlist
# Print linkedlist


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = newNode
            
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next



firstNode = Node("Rudalph")
linkedList = Linkedlist()
linkedList.insert(firstNode)


secondNode = Node("Gonsalves")
linkedList.insert(secondNode)

linkedList.printList()