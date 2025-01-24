def myfun():
    print("Hello world")
    
myfun()

print(__name__) # print __main__
                # Agar dusre file se call karoge tho __module__ print karega
                
if __name__ == "__main__":
    print("I will get printed when modul.py is executed")