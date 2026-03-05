# There is an array given —— which is nearly sorted means element at i is present at i-1 or i+1
# We need to search for an element in the array
# We will use binary search to search.

# Note —— Whenever you are clueless compare with what you know about that topic.

# Here we will apply standard binary search logic.
# We will compare the element with the middle element along with the elements at mid-1 and mid+1.
# Rest logic remains the same.

arr = [5, 10, 30, 20, 40]
ele = 40

start = 0
end = len(arr) - 1

while start <= end:
    mid = start + (end-start)//2

    if arr[mid] == ele:
        print(f"Element {ele} found at index {mid}.")
        break
    elif mid-1 >= start and arr[mid-1] == ele:
        print(f"Element {ele} found at index {mid}.")
    elif mid+1 <= end and arr[mid+1] == ele:
        print(f"Element {ele} found at index {mid+1}.")
    else:
        if ele < arr[mid]:
            end = mid - 2
        else:
            start = mid + 2


