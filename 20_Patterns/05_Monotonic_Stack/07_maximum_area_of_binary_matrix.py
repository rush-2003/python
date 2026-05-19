# Whtch the Video to understand the question: https://www.youtube.com/watch?v=St0Jf_VmG_g&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=8
# This question is a follow up of the question "Maximum Area of Histogram". 
# We will be using the same logic to solve this question. 
# The only difference is that we will be building the histogram for each row of the matrix and then finding the maximum area for that histogram.
# Every time we move to the next row, we will update the histogram by adding 1 to the previous histogram if the current cell is 1, otherwise we will reset it to 0.

def maximumAreaOfHistogram(arr):
    NSR = []
    stack = []
    for i in range(len(arr)-1, -1, -1):
        if not stack:
            NSR.append(-1)
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if stack:
                NSR.append(stack[-1][1])
            else:
                NSR.append(-1)
        stack.append((arr[i], i))

    NSR.reverse()
    # print(f"NSR: {NSR}")
    
    NSL = []
    stack = []
    for i in range(len(arr)):
        if not stack:
            NSL.append(-1)
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if stack:
                NSL.append(stack[-1][1])
            else:
                NSL.append(-1)
        stack.append((arr[i], i))

    # print(f"NSL: {NSL}")
    
    area = 0
    for i in range(len(arr)):
        length = arr[i]
        right = NSR[i] if NSR[i] != -1 else len(arr)
        left = NSL[i]
        width = right - left - 1
        area = max(area, length * width)
    return area
    
matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0]
]

row = len(matrix)
col = len(matrix[0])

max_area = 0

histogram = [0]*col
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            histogram[j] = 0
        else:
            histogram[j] += 1
    print(f"Histogram: {histogram}")
    max_area = max(max_area, maximumAreaOfHistogram(histogram))
    print(f"Max Area: {max_area}")