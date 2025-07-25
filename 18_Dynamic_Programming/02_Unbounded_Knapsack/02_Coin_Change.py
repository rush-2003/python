#Coin Change Problem : Number of Ways

#Problem Statement
#You are given an array of coins and a target and your task is to find the number of ways
#such that the coins can be added up to get the target. You can use the coins infinite times

#variables
arr = [1,2,5]
target = 11

#table formation
row = len(arr)+1
col = target + 1
dp = [[None for i in range(col)] for i in range(row)]

#table initilization
for i in range(row):
    for j in range(col):
        if i == 0:
            dp[i][j] = 0  
        if j == 0:
            dp[i][j] = 1

#core implementation
for i in range(1, row):
    for j in range(1, col):
        if arr[i-1] <= j:
            dp[i][j] = dp[i][j-arr[i-1]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[row-1][col-1])