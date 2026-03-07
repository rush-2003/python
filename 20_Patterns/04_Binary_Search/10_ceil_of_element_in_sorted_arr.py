# Ceiling of an element in a sorted array
# We are given a sorted array and a target element
# We need to find the ceiling of the target element in the array
# If that element is present in the array, then return that element
# If not, then return the smallest element greater than the target element

arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
target = 5

start = 0
end = len(arr)-1
ans = -1                
while start <= end:
    mid = start + (end-start)//2
    if arr[mid] == target:
        print(f"Element {target} found at index {mid}.")
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        ans = arr[mid] 
        end = mid - 1
print(f"Ceiling of {target} is {ans}.")