arr = []

def inorderTraversal(root, depth=0):
    if not root:
        return

    # Track entering left subtree
    print(f"{'  ' * depth}Entering left subtree of node {root.val}")
    print(depth)
    inorderTraversal(root.left, depth + 1)
    
    # Track the current node (add to array)
    print(f"{'  ' * depth}Visiting node {root.val}")
    print(depth)
    arr.append(root.val)
    
    # Track entering right subtree
    print(f"{'  ' * depth}Entering right subtree of node {root.val}")
    print(depth)
    inorderTraversal(root.right, depth + 1)
    
    # Track backtracking from current node
    print(f"{'  ' * depth}Backtracking from node {root.val}")

# Sample input tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Construct the tree: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Call the function
inorderTraversal(root)
print("Final array:", arr)
