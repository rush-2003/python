# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' 
# before each integer in nums and then concatenate all the integers.

'''
1. Suppose two sub arrays A. All +ve [Sub_arr_1] and B. All -ve [Sub_arr_2]
2. Take out '-' common from [Sub_arr_2]
3. [Sub_arr_1] - [Sub_arr_3] = Given Target
4. Problem is same as Count of Subset Sum
'''
nums = [1,1,1,1,1]
target = 3
tar = (target + sum(nums)) // 2
arr = nums

#matrix formation
row = len(arr) + 1
col = tar + 1
dp = [[None for i in range(col)] for i in range(row)]

#initilization of Matrix
for i in range(row):
    for j in range(col):
        if i == 0:
            dp[i][j] = 0
        if j == 0:
            dp[i][j] = 1

#implementation
for i in range(1,row):
    for j in range(1,col):
        if arr[i-1] <= j:
            dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[row-1][col-1])
        