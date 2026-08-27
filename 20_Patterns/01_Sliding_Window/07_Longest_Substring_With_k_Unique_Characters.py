'''
Longest Substring With k Unique Characters
Given a string and an integer k, 
find the length of the longest substring that contains exactly k unique characters.
'''


string = "aabacbebebe"
k = 3

i = 0
j = 0
max_length = 0
dicts = {}

while j < len(string):
    if string[j] not in dicts:
        dicts[string[j]] = 1
    else:
        dicts[string[j]] += 1
        
    if len(dicts) == k:
        max_length = max((j-i+1), max_length)
    elif len(dicts) > k:
        while len(dicts) > k:
            dicts[string[i]] -= 1
            if dicts[string[i]] == 0:
                del dicts[string[i]]
            i += 1
    if len(dicts) == k:
        max_length = max(max_length, j - i + 1)
    j += 1
    
print(max_length)