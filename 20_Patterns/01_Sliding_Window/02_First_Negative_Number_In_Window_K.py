# arr = [12, -1, -7, 8, -15, 30, 13, 28]
# k = 3

# indices = []
# for i in range(len(arr)):
#     if arr[i] < 0:
#         indices.append(i)
# print(f"Indices of negative numbers: {indices}")
# p = 0

# answer = []

# # Window
# i = 0
# j = k-1

# for l in range(k-1, len(arr)):
#     while p<len(indices) and indices[p]<i: #skip all the elements to the left of the window
#         p = p + 1
#     if p < len(indices) and indices[p] <= j:
#         answer.append(arr[indices[p]])
#     else:
#         answer.append(0)
#     i = i+1
#     j = j+1
# print(answer)


arr = [12, -1, -7, 8, -15, 30, 13, 28]
k = 3
i = 0
j = 0
neg = []
ans = []
while j <= len(arr)-1:
    if arr[j] < 0:
        neg.append(arr[j])
    
    if (j-i+1) != k:
        j = j + 1
    else:
        if len(neg)>0:
            ans.append(neg[0])
        else:
            ans.append(0)
        if neg and arr[i] == neg[0]:
            neg.pop(0)
        i = i + 1
        j = j + 1
print(ans)