# Find the first and last occurance of an given element

arr = [2, 4, 10, 10, 10, 18, 20]
ele = 10

start = 0
end = len(arr)-1

first_occurance = -1
last_occurance = -1

while start <= end:
    mid = start + (end-start)//2

    if arr[mid] == ele:
        first_occurance = mid
        end = mid-1
    elif ele < arr[mid]:
        end = mid-1
    else:
        start = mid+1

start = 0
end = len(arr)-1

while start <= end:
    mid = start + (end-start)//2

    if arr[mid] == ele:
        last_occurance = mid
        start = mid+1
    elif ele < arr[mid]:
        end = mid-1
    else:
        start = mid+1

print(f"First occurance: {first_occurance}")
print(f"Last occurance: {last_occurance}")

print(f"Count of {ele} is {last_occurance-first_occurance+1}")