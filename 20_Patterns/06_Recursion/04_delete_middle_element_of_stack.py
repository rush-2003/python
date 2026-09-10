# We are given a stack
# We have to find out the middle element and delete it
# If stack length is odd then we have proper middle element
# If stack length is even then formula is (k-1)/2 where k is the length of the stack

stack = [1, 2, 3, 4, 5, 6]

if len(stack) % 2 == 0:
    middle_index = (len(stack) - 1) // 2
else:
    middle_index = len(stack) // 2
    
def delete_middle_index(arr,middle_index):
    if middle_index == 0:
        arr.pop()
        return
    temp = arr.pop()
    delete_middle_index(arr, middle_index - 1)
    arr.append(temp)

delete_middle_index(stack, middle_index)
print(stack)

# Logic:
# We are using Base Condition - Hypotheses -Induction Method
# We cant think of decision so we work on making input smaller
# There are two inputs - stack and middle_index
# Stack will be reduced by popping the top element and middle_index will be reduced by 1
# So we get our base condition when middle_index is 0, we pop the top element and return

# Hypotheses:
# we have function that will take (arr, middle_index) and it will delete the middle element
# Now if we reduce the middle_index by 1 and pop the top element, we will have a smaller input

# Induction:
# Now we will call the function again with smaller input and it will delete the middle element
# After that we will append the popped element back to the stack and return
