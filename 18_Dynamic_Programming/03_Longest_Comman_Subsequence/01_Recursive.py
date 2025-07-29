a = "abcdgh"
b = "abedfhr"

def lcs(a, b, m, n):
    #Base Condition
    if m == 0 or n == 0:
        return 0
    
    #Choice Diagram
    if a[m-1] == b[n-1]:
        return 1 + lcs(a, b, m-1, n-1)
    else:
        return max(lcs(a,b,m-1, n), lcs(a,b,m,n-1))
    
print(lcs(a,b,len(a),len(b)))