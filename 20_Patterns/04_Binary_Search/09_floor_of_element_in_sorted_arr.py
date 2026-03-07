# We are given an sorted array
# We need to find the floor of a given element
# Now floor of 7.8 is 7 and ceil is 8

# We are given a sorted array and a target element
# We need to find the floor of the target element in the array
# If that element is present in the array, then return that element
# If not, then return the greatest element less than the target element

# Just apply normal BS
# But possible candidate will be found when arr[mid] < target —— in case if floor
# And possible candidate will be found when arr[mid] > target —— in case if ceil

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
        ans = max(ans, arr[mid])
        start = mid + 1
    else:
        end = mid - 1
print(f"Floor of {target} is {ans}.")

