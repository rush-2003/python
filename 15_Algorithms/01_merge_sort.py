def merge(arr, start, mid, end):
    temp = []
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i = i + 1
        else:
            temp.append(arr[j])
            j = j + 1
            
    while i<= mid:
        temp.append(arr[i])
        i = i + 1
        
    while j<= end:
        temp.append(arr[j])
        j = j + 1
        
    # Copy back to original array
    for i in range(len(temp)):
        arr[start + i] = temp[i]
            
        
    

def mergesort(arr, start, end):
    if start < end:    
        mid = start + (end - start)//2
        #left
        mergesort(arr, start, mid)
        #right
        mergesort(arr, mid+1, end)
        
        #merge
        merge(arr, start, mid, end)

arr = [4, 3, 2, 0, 1, 0]
mergesort(arr, 0, len(arr)-1)
print("Sorted array:", arr)