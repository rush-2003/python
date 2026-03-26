# Given an array
# The array is bitonic
# Bitonic means —— Monotonically increasing then monotonically decreasing
# Montonic means arr[i] != arr[i+1]

# Given such array we need to find the peak element in that array
# Peak element would be definately the element which is grater than prev and next

# So we will apply binary search
# Calculate mid and check its prev and next element if mid is greater than both then its arr[mid] is answer
# Else we need to go either left or right
# If we check carefully this is the same problem as peek_element.py


arr = [1, 3, 8, 12, 4, 2]
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