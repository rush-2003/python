# We have two strings
# a: AGGTAB and b: GXTXAYB
# Shortest Common Supersequence means - make a string such that it should have both the strings
# No continous but order should be maintained

'''
a: AGGTAB
B: GXTXAYB

Now the point is LCS is common in both 
So what you do is

1. Find the length of longest common subsequence
2. Merge the two strings : merged_string
3. answer = merged_string_length - lcs
'''