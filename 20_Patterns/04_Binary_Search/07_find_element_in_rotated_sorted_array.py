arr = [11, 12, 13, 15, 18, 2, 5, 6, 8]
ele = 15

start = 0
end = len(arr)-1

while start <= end:
    mid = start + (end-start) // 2
    if arr[mid] == ele:
        print(f"Element {ele} is present at indedx {mid}")
        break
    if arr[start] <= arr[mid]:
        if arr[start] <= ele < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else:
        if arr[mid] < ele <= arr[end]:
            start = mid + 1
        else:
            end = mid - 1

# My own logic
# Apply binary search
# compare (start, mid) and (mid, end)
# Check which is sorted and if element lies in sorted section
# Update start and end accordingly

# Video logic
# We know how to calculate minimum value's index
# Thus we get 2 sorted arrays
# Apply binary search on both
# 1 array will return -1 and other array will return an index — That;s our answer
# if both arrays return -1 that means element is not present in the array