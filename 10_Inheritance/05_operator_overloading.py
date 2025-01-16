# Operator overloading in Python allows developers to redefine the behavior of built-in operators (like +, -, *, etc.) for user-defined classes. 
# This enables objects of your classes to interact using operators in a meaningful way.



# Python allows operator overloading by defining special methods (also called dunder methods, short for "double underscore"). 
# These methods start and end with double underscores, e.g., __add__, __sub__, __eq__.


# For example:

# + is implemented using the __add__ method.
# - is implemented using the __sub__ method.
# * is implemented using the __mul__ method.


class Number:
    def __init__(self, n1):
        self.n1 = n1
        
    def __add__(self, num):
        return print("me",self.n1 + num.n1)
        
no1 = Number(1)
no2 = Number(2)

print(no1.n1 + no2.n1) # Right way

# print(no1 + no2) -> Error before __add__ 


