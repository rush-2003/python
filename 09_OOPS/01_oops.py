# Object Oriented Programming is a Approach to solve problems in programming
# Works on princple DRY (Don't Repeat yourself)
# Using reusable code is programming

# 2 components 1) Class 2) Objects
# Class is Blueprint of Objects

# Class defined == info is defined
# Object initilized memory allocated

# Objects can invoke methods available in class without reveling the implemetation
# It is called abstraction and encapsulation

class Employee:
    name = "Rudalph"
    language = "Python"
    Salary = 1200000
    
Rudalph = Employee()
Rudalph.hobby = "Karate"
Rudalph.Salary = 100000000
print(Rudalph.name, Rudalph.language, Rudalph.Salary, Rudalph.hobby)

# Hobby is -> Object attribute / Instance attribute
# Salary, Name, Language -> Class attribute
# Instance attribute take preference over class attribute thus 100000000 >> 1200000