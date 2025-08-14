# PS says that 
# We have to find a palindromic string
# In such a way that 
# To convert the original string to palindromic
# The number of Interstions should be minimum


'''
1. Its very easy and entirly based on the problems that we have previously solved

2. Find Longest Palindromic Subsequence
3. We need two main components: A = 1st-len(original_string) B = 2nd-len(palindromic_string)
4. number_of_insertions = A - B
'''

# For eg: str_orig = "aebcbda"
# To find Longest Palindromic Subsequence we will use LCS
# We need 2nd string which is reverse of original str_rev = "adbcbea"
# LPS = "abcba"
# ans = len(str_orig)[7] - len(str_rev)[5] = 2
# Now to make aebcbda palindromic I will need to add two characters more in it 'e' and 'd'