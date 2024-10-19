#Dictionaries : Key value pairs are saved
# Unordered
# Mutable
# Indexed (based on keys)
# No Duplicate Keys

d = {}  # Empty dictionary

marks = {
    "harry" : 56,
    "Rudalph" : "100",
    list : [1,2,3,4]
}
#print(marks[0]) -> error


print(marks , type(marks))
print(marks["Rudalph"])
print(marks[list][0])


marks1 = {
    "harry" : 56,
    "Rudalph" : "100",
    "list" : [1,2,3,4]
}
print(marks["list"][0])