lists = ["Rudalph", 7, False, "Gonsalves"]
print(lists)
lists.append("Good")
print(lists)

numbers = [10, 30, 5, 25, 8,10,10,10]
numbers.sort()
print(numbers)

alphabets = ['a', 'D', 'd', 'x', 'c']
alphabets.sort()
print(alphabets)

numbers.reverse()
print(numbers)

numbers.insert(3, "Rudalph")
print(numbers)

#removes by index 
x=numbers.pop(4)
print(x)
print(numbers)

#removes by value the 1st occurrance, returns nothing
x=numbers.remove(10) , 
print(x)
print(numbers)

