# Creating new class from existing one

class Employee:  # Base Class / Parent Class 
    name = "Rudalph"
    
    def show(self):
        print(f"The name is {self.name}")
        

class Programmer1:
    name = "Rudalph"
    data = 7249735828
    def show(self):
        print(f"The name is {self.name}")    
        
    def show_data(self):
        print(f"The name is {self.data}")
        
class Programmer2(Employee):  # Derived Class / Child Class
    data = 7249735828
    
    def show_data(self):
        print(f"The name is {self.data}")
 
        
a = Employee()
a.show()

b = Programmer1()
b.show()
b.show_data()

c = Programmer2()
c.show()
c.show_data()

# 1. Single Inheritance (we just saw above)

# 2. Multiple Inheritance
class Dad:
    def display_dad(self):
        print("I am dad") 

class Mom:
    def display_mom(self):
        print("I am Mom") 
        
class Child(Dad, Mom):
    def display_child(self):
        print("I am child")
        
c1 = Child()
c1.display_dad()
c1.display_mom()
c1.display_child()

# 3. Multilevel Inheritance
class cls1:
    def display_dad(self):
        print("I am dad") 

class cls2(cls1):
    def display_mom(self):
        print("I am Mom") 
        
class cls3(cls2):
    def display_child(self):
        print("I am child")