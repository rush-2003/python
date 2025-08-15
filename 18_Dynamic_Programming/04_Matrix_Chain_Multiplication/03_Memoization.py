# size of dp matrix is to be otbained from constraints
# eg: constraints says 1000 the mxn = 1001 x 1001

arr = [40, 20, 30, 10, 30]

row = 100
col = 100

dp = [[-1 for i in range(col)] for i in range(row)]

def solve(arr, i, j):
    if i >= j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    mini = float('inf')
    
    for k in range(i, j):
        temp_ans = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
        if temp_ans < mini:
            mini = temp_ans
    
    dp[i][j] = mini        
    return dp[i][j]

result = solve(arr, 1, len(arr)-1)
print(result)