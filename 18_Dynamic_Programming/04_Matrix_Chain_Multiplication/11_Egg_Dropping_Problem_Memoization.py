# PS says we have e (eggs) and a building of f (floors)
# We have to drop the eggs from the builing 
# Find that floor from which when the egg is dropped it dosent break
# Lets suppose
# e=3 and f=7 and k is that floor
# We have to find minimum number of attempts of worst case - Confusing(Watch video its very easy)

e = 3
f = 7

row = 100
col = 100
dp = [[-1 for i in range(col)] for i in range(row)]


def solve(e, f):
    if f==0 or f==0:
        return f
    if e == 1:
        return f
    
    if dp[e][f] != -1:
        return dp[e][f]
    
    mini = float('inf')
    
    for k in range(1, f+1):
        temp = 1 + max(solve(e-1, k-1), solve(e, f-k))
        mini = min(mini, temp)
        
    dp[e][f] = mini        
    return dp[e][f]

print(solve(e,f))

'''
There is more optimized version of this Memoization in Video
Watch that again
'''