# Top k frequent numbers
import heapq

dicts = {}

arr = [1,1,1,3,3,3,3,3,3,3,3,3,3,2,2,4,5,5,5,5,5,5,5,5,5,5]
k = 2

for i in arr:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1

min_heap = []
for i in dicts:
    heapq.heappush(min_heap, (dicts[i], i))
    if len(min_heap)>k:
        heapq.heappop(min_heap)
print(min_heap)