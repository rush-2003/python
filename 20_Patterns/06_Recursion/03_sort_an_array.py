# We are given an array of integers, we need to sort the array using recursion.
# Recurssion Technique: Base Condition - Hypotheses - Induction

# In this question we can't think of primary step - Taking Decision
# Thus we will go with secondary setp - Making input smaller

# Input is array lets say [5, 4, 3, 2, 1]
# Smaller input: [5, 4, 3, 2] and [1]
# Even Smaller input: [5, 4, 3] and [2] and [1]

# Thus what is the base condition? 
# When the array has only one element, it is already sorted.

# Next comes Hypotheses
# we have a function sort_array(arr) which sorts the array arr.
# input given [5, 4, 3, 2, 1] output should be [1, 2, 3, 4, 5]
# When smaller input is given [5, 4, 3, 2] output should be [2, 3, 4, 5]

# Next comes Induction
# We have a function sort_array(arr) which sorts the array arr. 
# In induction step we will take the last element of the array and insert it in the sorted array of smaller input.
# But how?
# We need another recurssion for insert function - That we will discuss later

def sort_array(arr):
    # Base condition:
    if len(arr) <= 1:
        return arr
    
    # Hypotheses:
    ele = arr.pop()
    sorted_arr = sort_array(arr)
    
    # Indution
    # We can use another recurssion to insert the element in the sorted array
    # Or we can use for loop to insert the element in the sorted array
    
    # We will go with recurssion
    inserted_arr = insert_in_sorted_array(sorted_arr, ele)
    return inserted_arr

def insert_in_sorted_array(arr, ele):
    # Base condition:
    if len(arr) == 0 or arr[-1] <= ele:
        arr.append(ele)
        return arr
    
    # Hypotheses:
    last_ele = arr.pop()
    sorted_arr = insert_in_sorted_array(arr, ele)
    
    # Induction
    sorted_arr.append(last_ele)
    return sorted_arr

print(sort_array([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]