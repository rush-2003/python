# Problem Statement: https://leetcode.com/problems/climbing-stairs/description/


'''Climbing Stairs Recursion'''
arr = [0]
def climbing_stairs(n):
    if n == 0:
        arr[0] += 1
        return
    if n < 0:
        return
    climbing_stairs(n-1)
    climbing_stairs(n-2)
    
climbing_stairs(4)
print(arr[0])



'''Climbing Stairs Memoization'''
def climbing_stairs_memoization(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = climbing_stairs_memoization(n-1, memo) + climbing_stairs_memoization(n-2, memo)
    return memo[n]
print(climbing_stairs_memoization(4, [-1]*5))



'''Climbing Stairs Tabulation'''
def climbing_stairs_tabulation(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1]
        if i > 1:
            dp[i] += dp[i-2]
    return dp[n]
print(climbing_stairs_tabulation(4))