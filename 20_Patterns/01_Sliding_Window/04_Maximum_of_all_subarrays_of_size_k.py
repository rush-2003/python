arr = [1,3,-1,-3,5,3,6,7]
size = 3
i = 0
j = 0
maxi = arr[0]
maxi_index = 0
ans = []
while j < len(arr):
    if j < size:
        if arr[j] > maxi:
            maxi = arr[j]
            maxi_index = j
        j += 1
    else:
        ans.append(maxi)
        i += 1
        j += 1
        if arr[j] > maxi:
            maxi = arr[j]
            maxi_index = j
        else:
            if i >= maxi_index and maxi_index <= j:
                pass
            else:
                while maxi_index < j:
                    maxi_index += 1
                    if arr[maxi_index] > maxi:
                        maxi = arr[maxi_index]
                        maxi_index = maxi_index

print(ans)
