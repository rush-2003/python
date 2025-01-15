class Employee:
    name = "Rudalph"
    green_flag = True
    salary = 1200000
    
    def getInfo(self, aura):
        # print(f"The language is {language}") -> This will give errro
        print(f"The Salary is {self.salary} and {aura} ")
        
    def greet_1(self):
        print("Hello I am greet 1")
        
    @staticmethod
    def greet_2():
        print("Hey I am greet 2")
    
rudalph = Employee()
print(rudalph.name, rudalph.green_flag, rudalph.salary)

# When I call rudalph.getInfo() the call is like: Employee.getInfo(rudalph) -> So basically Object is going as argument
# To handle this we use 'self' kuch bhi use kar sakte hai lekin self use karte hai

rudalph.getInfo(1000) # Same as Employee.getInfo(rudalph)

# Abhi koi ek fun hai class mein jo class atributes nahi use kar raha
# Fir bhi jab hum use call lagayenge hum pura object uske andar pass kar rahe hai 
# Example agar greet_1 ko call kiya it will be Employee.greet_1(rudalph) || rudalph.greet_1()
# Aur greet_2 ko call kiya it will be Employee.greet_2() ==>> Static method (Object pass nahi karneka) || rudalph.greet_2()

rudalph.greet_1()
rudalph.greet_2()
    
    