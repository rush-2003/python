''' Fibonacci Recurssion Code'''

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(10))

# Dynamic Programming Identification
#  1. Overlapping Subproblems [Repeated subproblems]
#  2. Optimal Substructure [Results of smaller subproblems can be used to solve larger problems]

# Types of Dynamic Programming
# 1. Memoization [Top Down Approach] = Recursion + Data Structure

# 2. Tabulation [Bottom Up Approach] = Loops + Data Structure
# Tips to solve by tabulation:
#  - Define the data structure + Meaning (What are we gonna store)
#  - Initilize with known smallest values
#  - Start solving from small to big

# Notes:
# Memoization - Only valid states are calulated
# Tabulation - All states (Valid + Invalid) are calulated 

''' Fibonacci Memoization Code'''

def fibo_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
    return memo[n]

print(fibo_memo(12))

''' Fibonacci Tabulation Code'''
def fibo_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(fibo_tab(13))

''' Fibonacci Space Optimization Code'''
def fibo_space(n):
    if n <= 1:
        return n
    prev2 = 0
    prev1 = 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

print(fibo_space(14))