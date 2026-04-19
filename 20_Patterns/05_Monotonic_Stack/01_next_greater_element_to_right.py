# Problem Statement
# Given an array
# we need to find the next greater element to the right of each element in the array.

# Solution
# Traverse the array from right to left
# Use three different components
# 1. Question array
# 2. Answer array -> Where answeres are stored
# 3. Stack -> To store the elements

# Algorithm
# Basically traverse from right to left
# At every element we need to check its right side elements
# So we check stack 
# If stack is empty answer is -1
# If stack[-1] is greater than current element then answer is stack[-1]
# If stack[-1] is smaller than current element then pop the element from stack

arr = [1, 3, 2, 4]

ans = []
stack = []

for i in range(len(arr)-1, -1, -1):
    if stack and stack[-1]>arr[i]:
        ans.append(stack[-1])
    else:
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
    stack.append(arr[i])

ans.reverse()
print(ans)