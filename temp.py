def eliminate(arr, step=1):
    # print(f"Step {step} - length: {len(arr)}, first few: {arr[:10]}")
    if len(arr) == 1:
        return arr[0]

    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = None
    arr = [i for i in arr if i is not None]
    arr.reverse()
    return eliminate(arr, step + 1)
n = 1000000000
arr = []
for i in range(1, n+1):
    arr.append(i)
# print(arr)
print(eliminate(arr))