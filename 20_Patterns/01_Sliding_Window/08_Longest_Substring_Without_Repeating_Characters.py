'''
Given a string s, find the length of the longest substring without repeating characters.
'''


string = "abcabcbb"

char_set = set()
i = 0
j = 0
max_length = 0

while j < len(string):
    if string[j] not in char_set:
        char_set.add(string[j])
        j += 1
    else:
        max_length = max((j-i), max_length)
        while string[j] in char_set:
            char_set.remove(string[i])
            i += 1
        char_set.add(string[j])
        j += 1

max_length = max((j-i), max_length)
print(max_length)