# We are given a stack
# We have to reverse a stack

# We will be using Base Condition, Hypotheses and Induction menthod

# Hypotheses: fun([5, ,4, 3, 2, 1]) = [1, 2, 3, 4, 5]
# What if input is smaller, fun([5, 4, 3, 2]) = [2, 3, 4, 5]

# What is the base condition then?
# If the input is empty, then we can return the empty stack as it is already reversed.

# Now induction step
# We have to again go for recurssion
# We will implement insert function
# lets derive hypotheses for insert function
# insert([5, 4, 3, 2], 1) = [1, 5, 4, 3, 2]
# for smaller input, insert([5, 4, 3], 2) = [2, 5, 4, 3]
# What would be the base condition for insert function?
# If the input is empty, then we can return the stack with the element inserted as it is already reversed.
# Now induction step for insert function
# We will pop the top element and call insert function again with the smaller input and the element

stack = [5, 4, 3, 2, 1]
def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)
    
def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return
    top = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(top)
    
print("Original Stack:", stack)
reverse_stack(stack)    
print("Reversed Stack:", stack)

# Reverse stack function:keeps poping the elements from the stack until it is empty and then calls insert_at_bottom function to insert the popped elements at the bottom of the stack.
# Insert at bottom function: keeps poping the elements from the stack until it is empty and then inserts the element at the bottom of the stack and then pushes back the popped elements to the stack.
