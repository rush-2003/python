def rec(n):
    if n == 1:
        print(n)
        return
    print(n)
    rec(n-1)
    
rec(10 ) 