# PS says that we have a string a = "agbcba"
# We want to find a palindromic subsequence
# abcba : agbcba
# bcb   : agbcba
# b     : agbcba

# Now the plaindromic string should be such that number od deletions from the original string 
# Should be minimum

'''
1. It is only possible when the palindromic string is of maximum length

STEPS:
A. Find the length of largest palindromic subsequence
B. Final Answer = len(string) - LPS
'''