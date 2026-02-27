arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
ele = 3
start = 0
end = len(arr)-1

while start<=end:
    mid = start + (end-start) // 2
    if arr[mid] == ele:
        print(f"Element {ele} found at index {mid}")
    if ele < arr[mid]:
        start = mid + 1
    else:
        end = mid - 1