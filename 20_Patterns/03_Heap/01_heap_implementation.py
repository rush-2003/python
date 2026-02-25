# Identification
# K + Largest/Smallest
# K = heap size
# 2 types heap — min_heap | max_heap

# When to use which heap
# min heap — k + largest (min element on top)
# max heap — k + smallest (max element on top)

# representation = stack

# put elements in heap/stack
# remove smaller/larger elements that comes beyond the heap size (min, max respectively)
# top element is answer
 
# Heap questions are sorting questions — O(nlogn)
# with the help of k — O(nlogK)

# heapq is by default min heap

'''CHEAT SHEET'''
# heappush(h, x) insert
# heappop(h) remove smallest
# h[0] peek smallest
# heapify(h) in-place build heap
# heappushpop(h, x) push then pop smallest
# heapreplace(h, x) pop smallest then push x

'''https://www.geeksforgeeks.org/dsa/introduction-to-heap/'''

import heapq
arr = [7, 4, 10, 3, 20, 15]
k = 3
max_heap = []

for i in arr:
    heapq.heappush(max_heap, -i)
    if len(max_heap)>k:
        heapq.heappop(max_heap)
print(-max_heap[0])

import heapq
arr = [7, 4, 10, 3, 20, 15]
k = 3
min_heap = []

for i in arr:
    heapq.heappush(min_heap, i)
    if len(min_heap)>k:
        heapq.heappop(min_heap)
print(min_heap[0])