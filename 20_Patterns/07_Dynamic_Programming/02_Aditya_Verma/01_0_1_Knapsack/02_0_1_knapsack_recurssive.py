'''0 1 Knapsack'''

# We have a bag whose weight is W = 7
# We have a weight array = [1, 3, 4, 5]
# We have a value array = [1, 4, 5, 7]

# We have to take elements in the bag such that the
# Profit should be maximum and the weight should not exceed

arr = [0]
def knapsack_recursive(weight, value, capacity, profit, index):
    if index >= len(weight):
        arr[0] = max(arr[0], profit)
        return arr[0]
    
    var1 = 0
    # Take the element
    if capacity-weight[index] >= 0:
        var1 = knapsack_recursive(weight, value, capacity-weight[index], profit+value[index], index+1)
    
    # Don't take the element
    var2 = knapsack_recursive(weight, value, capacity, profit, index+1)
    
    return max(var1, var2)
    
print(knapsack_recursive([1,3,4,5], [1,4,5,7], 7, 0, 0))
print(arr[0])
        