# Identification and Basic code Format

# We will be given an Array or String
# We will need two pointers i->Left_end & j->Right_end 
# We will need a K pointer which is central pointer

'''
1. Break the array/string at K

2. Call the fucntion again with 2 arrays/strings as
   fun(arr, i, k) and fun(arr, k+1, j)
   
3. Through step 2 calculate temp_ans

4. Lastly based on temp_ans and apply some function and calculate final answer
''' 

# We will use recursive and memoization versions only
# Depending upon the questions
# Base conditions, values of i,j,k etc will keep on changing

'''Boiler Plate Code'''

def solve(arr, i, j):
    if j > i:
        return 0
    
    for k in range(i, j):
        temp_ans = solve(arr, i, k) or solve(arr, k + 1, j) #or will change to some other operation
        final_ans = min(temp_ans) #min will change to some other operation
        
    return final_ans