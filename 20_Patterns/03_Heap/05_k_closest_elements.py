# Integer K is given
# array is given
# an integer x is given

'''Problem Statement'''
# Find k closest element to integer x in given array

import heapq

arr = [5, 6, 7, 8, 9]
x = 7
k = 3

max_heap = []

for i in arr:
    heapq.heappush(max_heap, (-abs(x-i), -i))
    if len(max_heap) > k:
        heapq.heappop(max_heap)

ans = []
while max_heap:
    dist, val = heapq.heappop(max_heap)
    ans.append(-val)
print(ans)
