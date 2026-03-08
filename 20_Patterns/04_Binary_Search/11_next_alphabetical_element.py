# We are given an array sorted of alphabets
# Problem is same as finding ceil of a number in sorted array
# Like a key/target is given and we have to find the smallest element which is greater than key/target
# Only thing is even if the key/target is present then also we need to find the next smallest element grater than key


arr = ['a', 'c', 'f', 'h']
ele = 'f'

start = 0
end = len(arr) - 1

res = -1

while start <= end:
    mid = start + (end-start)//2
    if arr[mid] == ele:
        start = mid + 1
    elif ele < arr[mid]:
        res = arr[mid]
        end = mid -1
    elif ele > arr[mid]:
        start = mid + 1

print(res)