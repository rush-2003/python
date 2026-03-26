# Given a bitonic array
# We are given a key
# We need to find the key in the array

# Logic
# If we see the bitonic array
# Its clear that we can divide it into 2 seperate arrays
# 1st part would be sorted in ascending order
# 2nd part would be sorted in descrnding order
# Peak element is the one where division can be done
# This is all the elements before peak element are consider to be sorted in ascending order
# And all elements after peak including peak are considered to be sorted in descending order

# Thus find peak element
# Divide the Bitonic array into two parts
# Then apply BS on ascending and descending sorted array



# So this question is basically combination of 3 concepts which we have already covered
# 1. Finding peak element in bitonic array — File 15
# 2. Standard Binary Search — File 01
# 3. Binary Search on reverse sorted array — File 02
