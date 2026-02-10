arr = [1,2,3,1]

dp = [0]*len(arr)
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    dp[i] = max(dp[i-1], arr[i]+dp[i-2])

print(dp[-1])