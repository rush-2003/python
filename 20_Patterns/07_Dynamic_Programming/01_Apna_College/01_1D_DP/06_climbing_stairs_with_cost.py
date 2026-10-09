'''Recursive Code'''
cost  = [10, 20, 15, 5, 30]
def climbing_stairs_with_cost(i, cost):
    if i >= len(cost):
        return 0
    return cost[i] + min(climbing_stairs_with_cost(i+1, cost), climbing_stairs_with_cost(i+2, cost))

print(climbing_stairs_with_cost(0, cost))


# For LeetCode
# print(min(
#     climbing_stairs_with_cost(0, cost),
#     climbing_stairs_with_cost(1, cost)
# ))


'''Memoization Code'''
cost  = [10, 20, 15, 5, 30]
dp = [-1]*(len(cost)+1)

def climbing_stairs_with_cost(i, cost, dp):
    if i >= len(cost):
        return 0
    if dp[i] != -1:
        return dp[i]
    
    dp[i] = cost[i] + min(climbing_stairs_with_cost(i+1, cost, dp), climbing_stairs_with_cost(i+2, cost, dp))
    return dp[i]

print(climbing_stairs_with_cost(0, cost, dp))

# For LeetCode
# print(min(
#     climbing_stairs_with_cost(0, cost),
#     climbing_stairs_with_cost(1, cost)
# ))