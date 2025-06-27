def isSorted(arr, size):
    if size == 0 or size == 1:
        return True
    
    if arr[size-1] < arr[size-2]:
        return False
    
    return isSorted(arr, size-1)

arr = [5, 1, 4, 2]
print(isSorted(arr, len(arr)))  # Output: False
