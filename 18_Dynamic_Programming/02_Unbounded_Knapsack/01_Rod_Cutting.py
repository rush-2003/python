#THIS IS STANDARD UNBOUND KNAPSACK PROBLEM

# arr = [1,2,3,4] -> This is actually a rod of length N=4 and not array 
# price = [1,5,8,9]
# Maximize, Thus o/p = 10
# Cut the array in two pics such that the price is maximum

arr = [1,2,3,4]
price = [1,5,8,9]
#Output Maximize

row = 5 # n -> Length of array
col = 5 # N -> Length of Rod 
dp = [[None for i in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        if i == 0:
            dp[i][j] = 0
        if j == 0:
            dp[i][j] = 0
            
for i in range(1, row):
    for j in range(1, col):
        if arr[i-1] <= j:
            dp[i][j] =  max((price[i-1]+dp[i][j-arr[i-1]]), dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[row-1][col-1])