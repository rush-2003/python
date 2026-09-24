# We are given a integer n as input
# We are suppose to generate balanced parenthesis

# Let's say the number is 3
# so we have 3 closing brackets ( ( (
# and three openeing brackets ) ) )
# and 6 spaces _ _ _ _ _ _

# Every space has 2 choices - either closing bracket or opening bracket

# Watch the video again to understand recurssive tree - worth watching

# Notes
# 1. We will maintain open and close variable that tells us the count of parenthesis
# 2. Base condition: if open and close both are 0 then op is the answer
# 3. Opening bracket is always a choice if open != 0 
# 4. Closing bracket is not always a choice - its only the choice when close > open

# All the 4 pointers of notes will be understood once draw the recursive tree
# Watch the video again - worth watching 

def generate_balanced_parenthesis(opens, close, op):
    if opens == 0 and close == 0:
        print("".join(op))
        return
    
    if opens != 0:
        op1 = op[:]
        op1.append("(")
        generate_balanced_parenthesis(opens-1, close, op1)
        
    if close > opens:
        op2 = op[:]
        op2.append(")")
        generate_balanced_parenthesis(opens, close-1, op2)
        
n = 3
opens = 3
close = 3
op = []
generate_balanced_parenthesis(opens, close, op)