#Kadane’s Algorithm

arr = [-2,1,-3,4,-1,2,1,-5,4]

dp = [0] * len(arr)
dp[0] = arr[0]
ans = arr[0]
for i in range(1, len(arr)):
    dp[i] = max(arr[i], arr[i]+dp[i-1])
    ans = max(ans, dp[i])

print(ans)

