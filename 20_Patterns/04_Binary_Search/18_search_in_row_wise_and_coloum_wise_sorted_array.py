# We start searching form the top right corner
# If top right corner is greater than key 
# that means all the elements of that coloumns are useless
# And lets decrement j

# Similarly if the element at i, j is smaller than key that means
# We need to increment key
# Because the element can be somewhere down in the coloum

# Every time we have a choice either move left or move down
# This is because matrix is sorted row wise and coloum wise


arr = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]

key = 6

i = 0
j = len(arr[0])-1

ans = []

while (i>=0 and i<len(arr)) and (j>=0 and j<len(arr[0])):
    if arr[i][j] == key:
        ans.append(i)
        ans.append(j)
        break
    elif arr[i][j]>key:
        j -= 1
    elif arr[i][j]<key:
        i += 1

if ans:
    print(f"Element {key} found at index {ans[0]}, {ans[1]}")
else:
    print(f"Element {key} not present in the Matrix")