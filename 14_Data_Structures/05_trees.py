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
numbers = [10,11,9,12,8,13,7]
treeRootNode = BinarySearchTreeNode(numbers[0])
for element in range(1, len(numbers)):
    treeRootNode.add_child(numbers[element])

#Printing root node and child nodes    
# print(treeRootNode.data, treeRootNode.left.data, treeRootNode.right.data)



# Traversal Techniques
# 1. Pre Order = Root Left Right
# 2. In Order = Left Root Right
# 3. Post Order = Left Right Root

#Preorder traversal
print(treeRootNode.preorder_traversal())
 
#Inorder traversal
print(treeRootNode.inorder_traversal())

#Postorder traversal
print(treeRootNode.postorder_traversal())

#Search
print(treeRootNode.search(100))