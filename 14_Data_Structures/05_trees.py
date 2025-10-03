class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data: #insertion of node to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right: #insertion of node to the right
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    # def inorder_traversal(self):  # [Left Subtree]-[Root Node]-[Right Subtree]
    #     arr = []
        
    #     if self.left:
    #         left_element = self.left.inorder_traversal()
    #         arr.extend(left_element)
            
    #     arr.append(self.data)
        
    #     if self.right:
    #         right_element = self.right.inorder_traversal()
    #         arr.append(right_element)
        
    #     return arr
    
    # What is the difference between append and extend
    # a = [1,2]
    # a.append([3,4])
    # Result: [1,2,[3,4]]
    # a = [1,2]
    # a.extend([3,4])
    # Result: [1,2,3,4]
    
    def preorder_traversal(self):  # [Root Node]-[Left Subtree]-[Right Subtree]
            arr = []
            
            arr.append(self.data)
            
            if self.left:
                arr.extend(self.left.preorder_traversal())
            
            if self.right:
                arr.extend(self.right.preorder_traversal())
            
            return arr 
    
    def inorder_traversal(self):  # [Left Subtree]-[Root Node]-[Right Subtree]
            arr = []
            
            if self.left:
                arr.extend(self.left.inorder_traversal())
                
            arr.append(self.data)
            
            if self.right:
                arr.extend(self.right.inorder_traversal())
            
            return arr 
        
    def postorder_traversal(self):  # [Left Subtree]-[Right Subtree]-[Root Node]
            arr = []
            
            if self.left:
                arr.extend(self.left.postorder_traversal())
            
            if self.right:
                arr.extend(self.right.postorder_traversal())
                
            arr.append(self.data)
            
            return arr
        
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False    
        
    
#Making of Root Node    
# treeNode = BinarySearchTreeNode(5)
# print(treeNode.data, treeNode.left, treeNode.right)

#Adding a Child Node 
# treeNode.add_child(10)
# print(treeNode.data, treeNode.left, treeNode.right.data)

#Adding another Child Node
# treeNode.add_child(2)
# print(treeNode.data, treeNode.left.data, treeNode.right.data)





#Making a Tree out of array
numbers = [40, 20, 60, 10, 30, 50, 70]
treeRootNode = BinarySearchTreeNode(numbers[0])
for element in range(1, len(numbers)):
    treeRootNode.add_child(numbers[element])

#Printing root node and child nodes    
# print(treeRootNode.data, treeRootNode.left.data, treeRootNode.right.data)



# Traversal Techniques
# 1. Pre Order = Root Left Right
# 2. In Order = Left Root Right
# 3. Post Order = Left Right Root

# #Preorder traversal
# print(treeRootNode.preorder_traversal())
 
#Inorder traversal
print(treeRootNode.inorder_traversal())

#Postorder traversal
# print(treeRootNode.postorder_traversal())

# #Search
# print(treeRootNode.search(100))



#Depth First Search
'''
1. In DFS we needs stack so we use Recursive method
2. DFS can be tackled by three ways
   A. In Order Traversal
   B. Pre Order Traversal
   C. Post Order Traversal
3. So all 3 traversals are nothing but DFS in different ways
'''

#Breadth First Search
'''
1. In BFS we needs Queue so we use Iterative method
'''
def bfs(root):
    if root is None:
        return
    
    queue = [root]   # Start with Dad
    
    while len(queue) > 0:
        current = queue[0]      # First person in line
        print(current.val)      # Print 1st Element
        queue = queue[1:]       # Remove them from the line
        
        if current.left is not None:
            queue.append(current.left)    # Add left child
        
        if current.right is not None:
            queue.append(current.right)   # Add right child
            
            
            
#-----------------------
'''Deletion of Node in tree'''
'''Playing with Structure of tree'''
'''Heap (Min heap and Max heap) -> Easy Concept'''
'''Serilization and Deserilization'''
#-----------------------



# Deletion
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: No child
            if not root.left and not root.right:
                return None
            
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Two children
            # Option A: use inorder successor
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

            # Option B (alternative): use inorder predecessor
            # predecessor = self.findMax(root.left)
            # root.val = predecessor.val
            # root.left = self.deleteNode(root.left, predecessor.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node

    def findMax(self, node):
        while node.right:
            node = node.right
        return node
    
    
    
#Preorder Serilization
def serialize(node):
    if not node:
        return "#"
    return f"{node.val},{serialize(node.left)},{serialize(node.right)}"

