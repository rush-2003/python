a = "abcde"
b = "abfce"

ans = []
temp = []

row = len(a)+1
col = len(b)+1
dp = [[-1 for i in range(col)]  for i in range(row)]

def lcs(a, b, m, n, temp=[]):
    if m == 0 or n == 0:
        return 0
    
    if a[m-1] == b[n-1]:
        dp[m][n] = 1 + lcs(a, b, m-1, n-1)
        return dp[m][n]
    else:
        
        dp[m][n] = 0
        return dp[m][n]
    
print(lcs(a, b, len(a), len(b)))
print(ans)
