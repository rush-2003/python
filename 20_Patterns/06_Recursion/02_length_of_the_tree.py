# Following: Base Condition - Hypothesis - Induction method

# Tree given
# We have to find the length of the tree

def lengthOfTree(node):
    # Base Condition
    if not node:
        return 0
    
    # Hypothesis
    left = lengthOfTree(node.left)
    right = lengthOfTree(node.right)
    
    # Induction
    return 1 + max(left, right)