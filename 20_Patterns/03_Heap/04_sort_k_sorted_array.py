# An array is given
# integer K is given
# any element in arr at index i can be at i+k or i-k
'''index 0  1  2  3  4   5  6  '''
# arr = [6, 5, 3, 2, 8, 10, 9]
'''         |<----|----->|     '''
# element 2(index 3) can be at index 5 or index 1
# We need to sort the array

# Now which heap to use
# here no largest or smallest is given
# since we know k and sorting thus Heap is the pattern
# In such cases check for top element you want or which elements you want in heap (largest, smallest) or which elements you want to eliminate (largest or smallest)

import heapq

arr = [6, 5, 3, 2, 8, 10, 9]
k = 4

counter = 0
min_heap = []

for i in arr:
    heapq.heappush(min_heap, i)
    if len(min_heap)>k:
        arr[counter] = heapq.heappop(min_heap)
        counter += 1

while min_heap:
    arr[counter] = heapq.heappop(min_heap)
    counter += 1

print(arr)

