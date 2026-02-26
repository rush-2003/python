# Sorted Given —— Binary search applicable

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ele = 2

start = 0
end = len(arr)-1

while start<=end:
    mid = start + (end-start) // 2
    if arr[mid] == ele:
        print(f"Element {ele} is at index {mid}")
        break
    else:
        if ele < arr[mid]:
            end = mid-1
        else:
            start = mid+1

f'''
Why —— start + (end-start) // 2 and not simply (start + end)//2
To prevent interger overflow
int can store value upto 10^9
Now lets say start value is around 10^9 and end value is also around 10^9
So int variable 'mid' can store (start + end) now because its out of range
Thus if we use start + (end-start) // 2 that issue (integer overflow) is resolved
'''