# Given an rotated array —— We need to find how many times it is rotated
# Paper Logic: Compare(Actual Sorted Array, Given Array) —— index of min element of given array is the answer
# So task is to search for min element in rotated sorted array

# Now we can do it using binary search
# But there are two things
# 1. How we will identify which element is smallest
# 2. If current element is not sorted then which side to move left or right

# For first question: 'arr[prev] < arr[mid] < arr[next]' —— then its the min element code ends

# For second question
# compare (start, mid)-Section A and (mid, end)-Section B
# check which section is unsorted (which is not ascending) we need to search that section

arr = [11, 12, 15, 18, 2, 5, 6, 8]

start = 0
end = len(arr)-1

while start <= end:
    mid = start + (end-start)//2

    next = (mid + 1)%len(arr)
    prev = (mid+len(arr)-1)%len(arr)

    if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
        print(f"Array is rotated by {mid}")
        break
    elif arr[mid] <= arr[end]:
        end = mid - 1
    else:
        start = mid + 1