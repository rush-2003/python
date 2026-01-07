# Monotonic Stack Apporoach
arr = [2, 1, 3]
n = len(arr)
res = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    # Step A: Pop smaller or equal elements
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    
    # Step B: Set NGE if stack not empty
    if stack:
        res[i] = stack[-1]
    
    # Step C: Push current element onto stack
    stack.append(arr[i])
    
    # Debug print for this step
    print(f"i={i}, arr[i]={arr[i]}, stack={stack}, res={res}")
