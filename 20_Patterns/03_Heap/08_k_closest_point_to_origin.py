# K Closest Point to Origin
import heapq
from math import sqrt

arr = [[1,3], [-2,2], [5,8], [0,1]]
k = 2

max_heap = []

for i in arr:
    distance = sqrt(i[0]*i[0]+i[1]*i[1])
    heapq.heappush(max_heap, (-distance, i))
    if len(max_heap)>k:
        heapq.heappop(max_heap)
print(max_heap)