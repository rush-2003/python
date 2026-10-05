# Problem Statement: https://leetcode.com/problems/house-robber/description/

'''House Robber Recurssion'''
def solve(ip, op):
  if len(ip) == 0:
    return sum(op)

  # Taken
  op1 = op[:]
  ip1 = ip[:]
  op1.append(ip1[0])

  if ip1:
    ip1.pop(0)
  if ip1:
    ip1.pop(0)

  # Not Tak:en
  op2 = op[:]
  ip2 = ip[:]
  if ip2:
    ip2.pop(0)

  return max(solve(ip1, op1),
  solve(ip2, op2))

arr = [2,7,9,3,1]
op = []
print(solve(arr, op))



'''House Robber Memoization'''
def house_robber_memoization(ip, op, dp):
    if len(ip) == 0:
        return sum(op)
    
    if dp[len(ip)] != -1:
        return dp[len(ip)]
    
    # Taken
    op1 = op[:]
    ip1 = ip[:]
    op1.append(ip1[0])
    
    if ip1:
        ip1.pop(0)
    if ip1:
        ip1.pop(0)
    
    # Not Taken
    op2 = op[:]
    ip2 = ip[:]
    if ip2:
        ip2.pop(0)
    
    dp[len(ip)] = max(house_robber_memoization(ip1, op1, dp),
                        house_robber_memoization(ip2, op2, dp))
    
    return dp[len(ip)]

arr = [2,7,9,3,1]
op = []
dp = [-1] * (len(arr) + 1)
print(house_robber_memoization(arr, op, dp))


'''House Robber Tabulation'''
def house_robber_tabulation(ip):
    n = len(ip)
    if n == 0:
        return 0
    if n == 1:
        return ip[0]
    
    dp = [0] * n
    dp[0] = ip[0]
    dp[1] = max(ip[0], ip[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + ip[i])
    
    return dp[n-1]

arr = [2,7,9,3,1]
print(house_robber_tabulation(arr))