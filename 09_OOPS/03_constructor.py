class Employee:
    name = "Rudalph"
    green_flag = True
    salary = 1200000
    
    def __init__(self, name, green_flag, salary, hobby):
        self.name = name
        self.green_flag = green_flag
        self.salary = salary
        self.hobby = hobby
        print("I am creating object")
    
    def getInfo(self, aura):
        # print(f"The language is {language}") -> This will give errro
        print(f"The Salary is {self.salary} and {aura} ")
        
    def greet_1(self):
        print("Hello I am greet 1")
        
    @staticmethod
    def greet_2():
        print("Hey I am greet 2")
    
# rudalph = Employee()
# rudalph.hobby = "Karate"
# print(rudalph.name, rudalph.green_flag, rudalph.salary, rudalph.hobby)

# The methods that start with __fun-name__ are called dunder methods
# __init__ Dunder method are called automatically 

ruddi = Employee("Ruddi", True, 10000000000, "Karate")
print(ruddi.name, ruddi.green_flag, ruddi.salary, ruddi.hobby)