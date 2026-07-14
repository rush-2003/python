# We are given a stack
# On that stack we can perform push pon top functions
# At any point if asked for the minimum element we have to return the minimum element in the stack

# Logic:
# We will have one main stack
# We will have one supporting stack
# Whenever we push an element in the main stack we will check if that element is less than or equal to the top of the supporting stack
# If it is less than or equal to the top of the supporting stack then we will also push that element in the supporting stack
# Whenever we pop an element from the main stack we will check if that element is equal to the top of the supporting stack
# If it is equal to the top of the supporting stack then we will also pop that element from the supporting stack

arr = [3, 5, 2, 1, 1, -1]
main_stack = []
supporting_stack = []
for i in range(len(arr)):
    main_stack.append(arr[i])
    if len(supporting_stack) == 0 or arr[i] <= supporting_stack[-1]:
        supporting_stack.append(arr[i])
        
print(main_stack)
print(supporting_stack)