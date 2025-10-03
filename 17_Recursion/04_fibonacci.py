def fibo(a, b, counter):
    if counter == 2:
        return
    
    new_ele = a + b
    print(new_ele)
    fibo(b, new_ele, counter-1)
    
print(0)
print(1)    
fibo(0, 1, 4)


# Nth Number of Fibonacci Series
def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
        
    return fibo(num-1) + fibo(num-2)
    
print(fibo(2))
