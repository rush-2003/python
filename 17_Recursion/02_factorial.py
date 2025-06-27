def factorial(n):
    #4 x 3 x 2 x 1
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(4))