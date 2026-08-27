'''
Pick Toys problem, which is essentially the Longest Substring with at Most 2 Distinct Characters
'''

'''
This problem is reduced into
Longest Substring With k Unique Characters
Given a string and an integer k, 
find the length of the longest substring that contains exactly k unique characters.
Where k is 2 in this case.
'''


toys= "aabacbebebe"
k = 3

i = 0
j = 0
max_length = 0
dicts = {}

while j < len(toys):
    if toys[j] not in dicts:
        dicts[toys[j]] = 1
    else:
        dicts[toys[j]] += 1
        
    if len(dicts) == k:
        max_length = max((j-i+1), max_length)
    elif len(dicts) > k:
        while len(dicts) > k:
            dicts[toys[i]] -= 1
            if dicts[toys[i]] == 0:
                del dicts[toys[i]]
            i += 1
    if len(dicts) == k:
        max_length = max(max_length, j - i + 1)
    j += 1
    
print(max_length)