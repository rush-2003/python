# container to store values of any datatypes
#indexing from 0 and we can also do negative indexing
friends = ["Rudalph",7,False]
print(friends)
print(friends[0])

#Lists are mutable
#original list gets updated when changes are made unlike strings
friends[0]="Gonsalves"
print(friends)

print(friends[-1])

#slicing
print(friends[0:2])