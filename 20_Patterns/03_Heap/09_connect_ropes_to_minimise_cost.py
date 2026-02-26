# Array given with length of ropes
# We need to connect ropes
# when 2 ropes are connected then cost is sum of their length
# At any time to minimise the cost we need to sum up the two smalles rope lengths

import heapq

arr = [1,2,3,4,5]
min_heap = []

heapq.heapify(arr)

cost = 0

while len(arr) > 1:
    x1 = heapq.heappop(arr)
    x2 = heapq.heappop(arr)
    heapq.heappush(arr, x1+x2)
    cost = cost + x1+x2
print(arr)
print(cost)