# Given an unsorted array
# Return index of peak element
# Peak element —— element whose neighbours are smaller than current element
# There might be mutiple peak elements
# Firt element is called peak element if its next element is smaller than first element
# Last element is called peak element if its prev element is smaller than last element

# How to identify to apply we have to apply Binary Search
# We know start = 0 and end = len(arr)-1
# We calculate mid and compare mid with its prev and next elements
# If prev and next elements are smaller than mid than peak element is mid
# Else we have to either move left or right
# Which part left or right would look more promsing — Binary Search on Answer
# say 5, 10, 20 mid is 10, prev is 5 and next is 20
# mid is not peak
# going to left is useless because if we go on left [5] we know its next is 10 which is greater than it
# So going to right makes sense

arr = [5, 10, 15, 4]
start = 0
end = len(arr)-1

while start <= end:
    mid = start + (end-start)//2
    if mid > 0 and mid < len(arr)-1:
        if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
            print(f'Peak element is {arr[mid]} at index {mid}')
            break
        elif arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if mid == 0:
            if arr[mid] > arr[mid+1]:
                print(f'Peak element is {arr[mid]} at index {mid}')
                break
            else:
                print(f'Peak element is {arr[mid+1]} at index {mid+1}')
                break
        elif mid == len(arr)-1:
            if arr[mid] > arr[mid-1]:
                print(f'Peak element is {arr[mid]} at index {mid}')
                break
            else:
                print(f'Peak element is {arr[mid-1]} at index {mid-1}')
                break