strs = "aab"

def ispalindrome(strs, i, j):
    ori_arr = [strs[x] for x in range(i, j+1)]
    rev_arr = list(reversed(ori_arr))
    return ori_arr == rev_arr

row = 100
col = 100
dp = [[-1 for i in range(col)] for i in range(row)]

def solve(strs, i, j):
    if i >= j:
        return 0
    
    if ispalindrome(strs, i, j):
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    mini = float('inf')
    
    for k in range(i, j):
        temp_ans = 1 + solve(strs, i, k) + solve(strs, k+1, j) 
        if temp_ans < mini:
            mini = temp_ans
            
    dp[i][j] = mini        
    return dp[i][j]

result = solve(strs, 0, len(strs)-1)
print(result)


'''
There is more optimized version of this Memoization in Video
Watch that again
'''