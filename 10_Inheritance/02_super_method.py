class Dad:
    
    def __init__(self):
        print("constructor Dad")

    def display_dad(self):
        print("I am dad") 

class Mom:
    
    def __init__(self):
        print("constructor Mom")
        
    def display_mom(self):
        print("I am Mom") 
        
class Child(Mom):
    
    def __init__(self):
        print("constructor Child")
        
    def display_child(self):
        print("I am child")
    
o1 = Child()    
        
# If I make object of a class tho sirf uska constructor run hoga usne jisko inherit kiya hai uska constructor nahi run hoga
# For eg. agar child ka object banaya tho child ka constructor run hoga mom and dad ka nahi

# Agar mereko chiye ki super class ka constructor bhi run ho the do below

class Dad:
    
    def __init__(self):
        print("constructor Dad")

    def display_dad(self):
        print("I am dad") 

class Mom:
    
    def __init__(self):
        print("constructor Mom")
        
    def display_mom(self):
        print("I am Mom") 
        
class Child(Mom):
    
    def __init__(self):
        super().__init__()
        print("constructor Child")
        
    def display_child(self):
        print("I am child")

o2 = Child() 