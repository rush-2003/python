import heapq

arr = [1,1,1,3,2,2,4]

max_heap = []

dicts = {}
for i in arr:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1

for i in dicts:
    heapq.heappush(max_heap, (-dicts[i], -i))
ans = []
while max_heap:
    freq, val = heapq.heappop(max_heap)
    ans = ans + ([-val]*-freq)

print(ans)
    