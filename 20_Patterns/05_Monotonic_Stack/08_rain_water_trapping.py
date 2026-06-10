# We are given an array which represents height of buildings.
# In this buildings after rainfall the water is trapped between the buildings.
# We have to find the total amount of water that is trapped between the buildings.

# Logic
# We have to calculate water on the top of each building and add it to the total water.
# How do we do that?
# For every building we have to find the maximum height of the building to its left and right
# Then find the minimum of the two maximums and subtract the height of the current building from it.
# That will give us the water on the top of the current building.

# So the main step is to calculate 2 arrays left_max and right_max
# left_max[i] will store the maximum height of the building to the left of the current building
# right_max[i] will store the maximum height of the building to the right of the current building


arr = [3, 0, 0, 2, 0, 4]
left_max = [0] * len(arr)
right_max = [0] * len(arr)      

for i in range(len(arr)):
    if i == 0:
        left_max[i] = arr[i]
    else:
        left_max[i] = max(left_max[i-1], arr[i])
        
for i in range(len(arr)-1, -1, -1):
    if i == len(arr)-1:
        right_max[i] = arr[i]
    else:
        right_max[i] = max(right_max[i+1], arr[i])

total_water = 0
for i in range(len(arr)):
    total_water += min(left_max[i], right_max[i]) - arr[i]

print(total_water)