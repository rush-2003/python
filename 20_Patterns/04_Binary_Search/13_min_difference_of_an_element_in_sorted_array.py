# Sorted array is given
# We need to find the element in array whose diff with ele is minimum
# Logically either ceil or floor is the one that can be the answer
# Do binary search 2 times find floor once and ceil second time
# Do abs difference with element and check for min difference

# Important note
# When we do standard binary search and loop ends without finding the element
# at that case
# arr[start] is ceil
# arr[end] is floor


arr = [1, 3, 8, 10, 15]
ele = 12

# FLOOR
start = 0
end = len(arr)-1
floor = None

while start <= end:
    mid = start + (end-start)//2
    
    if arr[mid] == ele:
        floor = arr[mid]
        break
    elif ele < arr[mid]:
        end = mid - 1
    else:
        floor = arr[mid]
        start = mid + 1

# CEIL
start = 0
end = len(arr)-1
ceil = None

while start <= end:
    mid = start + (end-start)//2
    
    if arr[mid] == ele:
        ceil = arr[mid]
        break
    elif ele < arr[mid]:
        ceil = arr[mid]
        end = mid - 1
    else:
        start = mid + 1

# ANSWER
if floor is None:
    ans = ceil
elif ceil is None:
    ans = floor
else:
    ans = floor if abs(ele-floor) < abs(ele-ceil) else ceil

print("Minimum difference element:", ans)
print("Difference:", abs(ans-ele))