# Climbing stairs with cost

# Logic is if we are on i then will we go on i+1 or i+2

'''Recurssion'''
final_cost = [float('inf')]

def frog_jump(i, heights, total_cost):

    if i == len(heights) - 1:
        final_cost[0] = min(final_cost[0], total_cost)
        return

    # Jump 1 stair
    cost1 = abs(heights[i] - heights[i + 1])
    frog_jump(i + 1, heights, total_cost + cost1)

    # Jump 2 stairs
    if i + 2 < len(heights):
        cost2 = abs(heights[i] - heights[i + 2])
        frog_jump(i + 2, heights, total_cost + cost2)


heights = [20, 30, 40, 20]

frog_jump(0, heights, 0)

print(final_cost[0])