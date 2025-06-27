def fibo(a, b, counter):
    if counter == 2:
        return
    
    new_ele = a + b
    print(new_ele)
    fibo(b, new_ele, counter-1)
    
print(0)
print(1)    
fibo(0, 1, 4)
