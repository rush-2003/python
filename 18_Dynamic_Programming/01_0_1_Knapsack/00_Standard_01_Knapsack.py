# Standard 0/1 Knapsack Problem

wt = [1, 2, 3, 4]       # Weights of items
val = [1, 5, 8, 9]      # Values of items
n = len(wt)             # Number of items
W = 4                   # Capacity of the knapsack

row = n + 1
col = W + 1
dp = [[0 for j in range(col)] for i in range(row)]

# Building the DP table
for i in range(1, row):
    for j in range(1, col):
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]],  # Take item
                           dp[i-1][j])                        # Don't take item
        else:
            dp[i][j] = dp[i-1][j]                             # Can't take item

# Final answer
print("Maximum Value in 0/1 Knapsack:", dp[row-1][col-1])
