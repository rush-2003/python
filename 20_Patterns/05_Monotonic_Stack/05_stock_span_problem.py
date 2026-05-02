# Problem Statement
# Given an array of prices of a stock for each day
# We need to find the span of the stock for each day
# Span is the number of consecutive days before the current day
# for which the price of the stock is less than or equal to the price of the stock on the current day


# ================================================
# MY LOGIC
# ================================================
# arr = [30, 40, 50, 60, 35, 70]

# stack = []
# ans = []

# for i in range(len(arr)):
#     if not stack:
#         ans.append(1)
#     else:
#         counter = 1
#         temp = []
#         while stack and stack[-1] <= arr[i]:
#             temp.append(stack.pop())
#             counter += 1
#         stack.extend(temp)
#         ans.append(counter)
#     stack.append(arr[i])

# print(ans)


# ================================================
# VIDEO LOGIC
# ================================================
arr = [100, 80, 60, 70, 60, 75, 85]

stack = []
indicesOfNGE = []

for i in range(len(arr)):
    if not stack:
        indicesOfNGE.append(-1)
    else:
        while stack and stack[-1][0] <= arr[i]:
            stack.pop()
        if stack:
            indicesOfNGE.append(stack[-1][1])
        else:
            indicesOfNGE.append(-1)
    stack.append((arr[i], i))

ans = []
for i in range(len(arr)):
    ans.append(i - indicesOfNGE[i])

print(ans)