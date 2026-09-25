# We are given a integer n
# We have to generate n bit binary number
# The binary number should be such that its prefix should have 1's >= 0


# for example: n = 3
# so we have 3 places: _ _ _
# every place has 2 choices 0 or 1

# What are prefixes of a binary number 1010101
# - The entire number itself
# - 101010_
# - 10101 _ _
# - 1010 _ _ _
# - 101 _ _ _ _
# . . . etc

# Note: 1st choice can't be 0

# We can have 2 variables: ones and zeros that will hold the count of 0s and 1s.
# Base condition: When n == 0

# Notice
# Choice of 1 is always possible
# But choice of zero is not alwasy available: its only available when 1s > 0s

# This will understand once we understood the Recurssive Tree
# Watch the video again - Worth watching

def print_binary(zeros, ones, op, n):
    if n == 0:
        print("".join(op))
        return
    
    op1 = op[:]
    op1.append('1')
    print_binary(zeros, ones+1, op1, n-1)
    
    if ones > zeros:
        op2 = op[:]
        op2.append('0')
        print_binary(zeros+1, ones, op2, n-1)
        
op = []
zeros = 0
ones = 0
n = 3
print_binary(zeros, ones, op, n)