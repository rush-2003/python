arr = [2,5,6,7,4,2,8,9]
k = 3
i = 0
j = 0
sums = 0
maxi = float('-inf')
while j<len(arr):
    sums = sums + arr[j]
    if (j-i+1) < k:
        j += 1
    elif j-i+1 == k:
        maxi = max(maxi, sums)
        sums = sums - arr[i]
        i += 1
        j += 1

print(maxi)