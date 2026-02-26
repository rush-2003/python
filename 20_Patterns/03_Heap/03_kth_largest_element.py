# Kth Larget element in the array

import heapq

arr = [7, 10, 4, 3, 20, 15]
k = 3

min_heap = []

for i in arr:
    heapq.heappush(min_heap, i)
    if len(min_heap)>k:
        heapq.heappop(min_heap)

print(min_heap)