# PS says we have e (eggs) and a building of f (floors)
# We have to drop the eggs from the builing 
# Find that floor from which when the egg is dropped it dosent break
# Lets suppose
# e=3 and f=7 and k is that floor
# We have to find minimum number of attempts of worst case - Confusing(Watch video its very easy)

e = 3
f = 7

def solve(e, f):
    if f==0 or f==0:
        return f
    if e == 1:
        return f
    
    mini = float('inf')
    
    for k in range(1, f+1):
        temp = 1 + max(solve(e-1, k-1), solve(e, f-k))
        mini = min(mini, temp)
        
    return mini

print(solve(e,f))