string = "cbaebabacd"
pattern = "abc"

patternMap = {}

for char in pattern:
    if char in patternMap:
        patternMap[char] += 1
    else:
        patternMap[char] = 1


tempMap = {}
i, j = 0, 0

while j < len(string):

    if string[j] in tempMap:
        tempMap[string[j]] += 1
    else:
        tempMap[string[j]] = 1

    if j - i + 1 == len(pattern):

        if tempMap == patternMap:
            print(f"Anagram found at index: {i}")

        tempMap[string[i]] -= 1

        if tempMap[string[i]] == 0:
            del tempMap[string[i]]

        i += 1

    j += 1
