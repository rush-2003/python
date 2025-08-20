# Step 1: Base condition
# Step 2: Hypothesis: 
# left Sub-Tree ans and Right Sub-Tree ans
# Step 3: Induction
# Use answer from Hypothesis


def solve(root, result):
    # Base Condition (Depends on problem, May be different and multiple)
    if root == None:
        return 0
    
    left = solve(root.left, result)
    right = solve(root.right, result)
    
    # If node dont want to become ans
    temp = calculate_temp_ans() # 1 + max(left, right)
    # Else if it want to become ans the
    ans = funA(temp, some_relation)
    result = funB(result, ans)
    
    return temp 
    
    
print(solve(root, result))