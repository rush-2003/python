# given an array of numbers
# Each number = height of a bar in a histogram
# All bars have:
    # Same width = 1
    # Different heights
# We need to:
    # Find the largest rectangle area possible
    # Rectangle must be formed using continuous bars

# Solution
# Pick a bar
# Expand it in bot ways
# Check how much expansion is possible in both was
# Calulate area

# To check the expansion in both direction we can use
# Next Smaller Element to Right and Left (With their indices)

arr = [6, 2, 5, 4, 5, 1, 6]

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
print(f"NSR: {NSR}")


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

print(f"NSL: {NSL}")

area = 0
for i in range(len(arr)):
    length = arr[i]
    right = NSR[i] if NSR[i] != -1 else len(arr)
    left = NSL[i]
    width = right - left - 1
    area = max(area, length * width)
print(area)
