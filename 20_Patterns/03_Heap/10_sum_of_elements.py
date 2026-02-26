# sum of all the elements between k1th smallest and k2th smallest

import heapq

def kth_element(arr, k):
    max_heap = []
    for i in arr:
        heapq.heappush(max_heap, -i)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]

arr = [1,3,12,5,15,11]
first = kth_element(arr, 3)   # 5
second = kth_element(arr, 6)  # 15

total = 0
for i in arr:
    if first < i < second:    # strictly between
        total += i

print(total)  # 23
