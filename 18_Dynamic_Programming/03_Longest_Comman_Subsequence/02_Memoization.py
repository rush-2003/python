# MEMOIZATION or Bottom Up = Recursion + Matrix
# Top Down = Only Natrix

a = "abcdgh"
b = "abedfhr"

dp = [[-1 for i in range(len(b)+1)] for i in range(len(a)+1)]

def lcs(a, b, m, n):
    #Base Condition
    if m == 0 or n == 0:
        return 0
    
    if dp[m][n] != -1 :
        return dp[m][n]

    
    #Choice Diagram
    if a[m-1] == b[n-1]:
        dp[m][n] = 1 + lcs(a, b, m-1, n-1)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs(a,b,m-1, n), lcs(a,b,m,n-1))
        return dp[m][n]
    
print(lcs(a,b,len(a),len(b)))
print(dp[len(a)][len(b)])

# | Approach                   | Method    | Uses Recursion? | Uses Matrix? | Key Idea                                                                                |
# | -------------------------- | --------- | --------------- | ------------ | --------------------------------------------------------------------------------------- |
# | **Top-Down (Memoization)** | Recursive | ✅ Yes           | ✅ Yes        | Solve bigger problem using recursion, store subproblem results in a matrix (`dp[m][n]`) |
# | **Bottom-Up (Tabulation)** | Iterative | ❌ No            | ✅ Yes        | Solve all smaller subproblems first in a matrix, and build up to the final result       |

