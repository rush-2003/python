strs = "aab"

def ispalindrome(strs, i, j):
    ori_arr = [strs[x] for x in range(i, j+1)]
    rev_arr = list(reversed(ori_arr))
    return ori_arr == rev_arr

def solve(strs, i, j):
    if i >= j:
        return 0
    
    if ispalindrome(strs, i, j):
        return 0
    
    mini = float('inf')
    
    for k in range(i, j):
        temp_ans = 1 + solve(strs, i, k) + solve(strs, k+1, j) 
        if temp_ans < mini:
            mini = temp_ans
            
    return mini

result = solve(strs, 0, len(strs)-1)
print(result)