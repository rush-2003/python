# Given an sorted infinte array
# Given an key/target and we need to find the position of that element in that infinite array
# We know start —— It will be 0
# We don't know end —— As array is infinite
# Rest binary search will be as it is

# Take start as 0 and end as 1
# if key not between start and end then 
# make start as end ——and—— end as end*2
# Finally we will get start and end such that key lies in between them
# Now infinite array problem vanishes and we have proper start and end
# Apply Standard Binary Search 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #.........
key = 7

start = 0
end = 1

while key >= arr[end]:
    start = end
    end = 2 * end

while start <= end:
    mid = start + (end-start)//2

    if arr[mid] == key:
        print(f"Element {key} found at index {mid}")
        break
    elif key < arr[mid]:
        end = mid - 1
    elif key > arr[mid]:
        start = mid + 1
