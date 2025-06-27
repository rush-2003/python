def nsum(n):
    if n == 0:
        return 0
    return n + nsum(n-1)

print(nsum(4))