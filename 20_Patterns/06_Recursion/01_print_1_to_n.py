# Method : Base Condition - Hypothesis - Induction 
# This method is usually used in Trees and Linked List

# Mental Model
# 1. Important is what decision is to be taken and not to make input smaller
# 2. But if we don't know what is the decision is to be taken then we can think of making the input smaller

# There are 4 approaches to solve a recurssive problem
# 1. Recurssive Tree
# 2. Base Condition - Hypothesis - Induction
# 3. Choice Diagram
# There is one more which is not discussed

# What is Base Condition:
    # Smallest valid input
    # Largest invalid input
    
# What is Hypothesis:
    # What our function is gonna do?
    # The function is gonna do the same thing when the input is smaller
    
# What is Induction:
    # We need to use the result of smaller input
    
'''
format for BC-H-I method:

function {
    Base Condition;
    Hypotheses
    Induction
}
'''

# Simple Problems: Base Condition - Hypothesis - Induction
# Medium Problems: Recurssive Tree
# Hard Problems: Choice Diagram

# If u ever want to revise this just have a look at the 2nd problem (Length of Binary tree) from the playlist

def printNumbers(n):
    # Base Condition
    if n == 1:
        print(1)
        return
    
    # Hypothesis
    printNumbers(n-1)
    
    # Induction
    print(n) 
    
printNumbers(5)
