# PS says we have one string a = "agbcba"
# We have to find longest Plaindromic Subsequence
# Basically we have to find a subsequence that is palindrome and also longest palindome
# In our case we have few palindromes like bcb-(3), abcba-(5) = our answer (LPS)

'''
1. Now we got to know our PS is related to LCS
2. But in LCS we need 2 strings
3. Here we have only one string
4. Its obvious that 2nd string is hidden or is to be derived from string 1
5. We will get second string by reversing the 1st string 
'''

# *****************************************************

'''
1. Rest everything is same as Longest Common subsequence
'''