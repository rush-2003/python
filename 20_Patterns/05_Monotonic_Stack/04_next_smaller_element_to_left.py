arr = [4, 5, 2, 10, 8]

ans = []
stack = []

for i in range(len(arr)):
    if stack and stack[-1]<arr[i]:
        ans.append(stack[-1])
    else:
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
    stack.append(arr[i])
    
print(ans)