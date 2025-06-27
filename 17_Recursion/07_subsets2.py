finalset = set()
def subsets(arr, ans, i=0):
    if i == len(arr):
        finalset.add(tuple(ans))
        return
    
    #include
    ans.append(arr[i])
    subsets(arr, ans, i+1)
    
    #exclude
    ans.pop()
    subsets(arr, ans, i+1)

arr = [1,2,3,4]
ans = []
subsets(arr, ans, 0)
print(finalset)