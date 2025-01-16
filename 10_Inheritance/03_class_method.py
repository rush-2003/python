class Employee:
    a = 1
    
    def show(self):
        print(f"value of a is {self.a}")
        
e = Employee()
e.a = 45
e.show()

# Agar mereko chiye ki object attribute na print ho and class attribute print ho then do below

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"value of a is {cls.a}")
        
e1 = Employee()
e1.a = 45
e1.show()