arr = [40, 20, 30, 10, 30]

def solve(arr, i, j):
    if i >= j:
        return 0
    
    mini = float('inf')
    
    for k in range(i, j):
        temp_ans = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
        if temp_ans < mini:
            mini = temp_ans
            
    return mini

result = solve(arr, 1, len(arr)-1)
print(result)