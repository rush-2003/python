# Problem Statement: Same as house robber 1
# But there are 2 conditions:
# 1. You cannot rob two adjacent houses
# 2. The houses are in circular manner, i.e., the first and last houses are also adjacent.


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


def house_robber_2(arr):
        
    return max(solve(arr[:-1], []), solve(arr[1:], []))
    
print(house_robber_2([2,7,9,3,1]))

# For implementation of DP
# Changes will be done in solve function
# Same changes as we did in our house robber 1 implementation