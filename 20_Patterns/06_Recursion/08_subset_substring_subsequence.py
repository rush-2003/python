'''
Substring : "abc" - continous, order matters  

Subset : {a, b, c} - Non continous, order dosent matters

subsequence : "abcd" - Non continous, order matters
'''

# If problem says
# Print superset | print subset | print subsequence
# Solution to all these problems - Print subsets
# Bit not for Substring

# Variations
# 1. They might ask for unique subsets - use set
# 2. They may ask for lexicographical order - use array to store all sunsets and sort the array later


'''
Summing up

Powerset              |-    Duplicates -> We wont get unique subsets -> [We have to peing in normal order or lexicographical order]
Subset      ->     subset
Subsequence           |-    No Duplicates -> We will get unique subsets -> [We have to peing in normal order or lexicographical order]
'''
