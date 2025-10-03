# My Personal Approach
arr = [2, 1, 3]
stack = [-1]*len(arr)

for i in range(len(arr)-2, -1, -1):
    if stack[i+1] == -1:
        if arr[i] < arr[i+1]:
            stack[i] = arr[i+1]
        else:
            stack[i] = -1
    else:
        if arr[i] > stack[i+1]:
            stack[i] = -1
        else:
            stack[i] = stack[i+1]
            
print(stack)



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
