# PS is we want to convert string a to b
# We can dp two operations 1. Insertion and 2. Deletion

'''
String-A --> LCS --> String-B
heap     --> ea  --> pea
x: len=4   y: len=2  Z: len=3

Deletions =  x - y = 2 (h, p)
Insertions = z - y = 1 (p)

# position of char matters
'''

a = "heap"
b = "pea"

row = len(a)+1
col = len(b)+1

dp = [[None for i in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        if i==0 or j==0:
            dp[i][j] = 0
            
for i in range(1, row):
    for j in range(1, col):
        if a[i-1] == b[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
lcs = dp[row-1][col-1]
print("Insertions: ", abs(len(a)-lcs))
print("Deletions: ", abs(len(b)-lcs))



