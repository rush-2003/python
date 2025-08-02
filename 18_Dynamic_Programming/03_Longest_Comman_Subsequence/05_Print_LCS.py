# Basically here we want to print longest common sub sequence
# so we follow top down approach as it is and the we actually bactrack the table

a = "abcdgh"
b = "abedfhr"

row = len(a)+1
col = len(b)+1

dp = [[None for i in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        if i == 0 or j == 0:
            dp[i][j] = 0
            
for i in range(1, row):
    for j in range(1, col):
        if a[i-1] == b[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print(dp[row-1][col-1])

# Backtracking the table
i = row - 1
j = col - 1
string = []
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        string.append(a[i-1])
        i = i - 1
        j = j - 1
    else:
        if dp[i][j-1] > dp[i-1][j]:
            j = j -1
        else:
            i = i -1
            
print(string)
