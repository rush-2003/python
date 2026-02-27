# Lets say we don't know if array is asc sorted or desc sorted
# In that case check of len of arr is greater than 1
# if yes then check arr[0] > or < arr[1] —— This will decide which Binary Search will be applied
# if the len(arr) is equal to 1 then compare arr[0] with target if same return found else return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ele = 4

start = 0
end = len(arr)-1

if arr[0] < arr[1]:
    print("Ascending Binary Search Applied")
    while start<=end:
        mid = start + (end-start) // 2
        if arr[mid] == ele:
            print(f"Element {ele} is at index {mid}")
            break
        else:
            if ele < arr[mid]:
                end = mid-1
            else:
                start = mid+1
else:
    print("Descending Binary Search Applied")
    while start<=end:
        mid = start + (end-start) // 2
        if arr[mid] == ele:
            print(f"Element {ele} found at index {mid}")
        if ele < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
