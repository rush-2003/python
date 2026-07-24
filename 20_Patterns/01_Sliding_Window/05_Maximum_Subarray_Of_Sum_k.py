'''We need to return maximum length of subarray with sum equal to k.'''

arr = [4, 1, 1, 1, 2, 3, 5]
k = 5

i = 0
j = 0
max_sum = 0
length = 0

while j < len(arr):
    max_sum += arr[j]
    
    if max_sum == k:
        length = max(length, j-i+1)
    elif max_sum > k:
        while max_sum > k:
            max_sum -= arr[i]
            i += 1
        if max_sum == k:
            length = max(length, j-i+1) 
    j+= 1

print(length)