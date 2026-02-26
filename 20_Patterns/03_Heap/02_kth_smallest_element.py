# Kth Smallest Element

import heapq

k = 3
arr = [7, 10, 4, 3, 20, 15]

max_heap = []
for i in arr:
    heapq.heappush(max_heap, -i)
    if len(max_heap)>k:
        heapq.heappop(max_heap)

print(-max_heap[0])