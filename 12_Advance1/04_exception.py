# We use try except if we dont want the program to get crashed 
# if error occurs
# CRASH - JAHA ERROR AAYA USE NEECHE KA EXECUTE NAHI HOGA
try:
    a = int(input("Enter a number: "))

except ValueError as v:
    print(v)
    print("Hey its a value error")
    
except Exception as e:
    print(e)
    
print("End of the program")


# raising error
# program crashes after raising the error
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))


if(b==0):
    raise ZeroDivisionError("divisor can't be 0")
else:
    print(a/b)
  
#This line wont be executed if content of IF block is executed    
print("End of the program")


# Try with Else
# If try block gets executed then only Else block will get execute
try:
    a = int(input("Enter a number: "))
    
except Exception as e:
    print(e)
    
else: 
    print("I am inside else")
    
print("End of the program")


# Try with Finally
# Finally will execute and it has nothing to do with other blocks execution
try:
    a = int(input("Enter a number: "))
    
except Exception as e:
    print(e)
    
finally: 
    print("I am inside FINALLY")
    
print("End of the program")

# finally ka use function mein ata hai
def main():
    try:
        #code
        return
    except:
        #code
        return
    
    finally:
        print("_______") #upar return hua tho bhi ye print hoga
    
    print("_____") #upar return hua tho ye print nahi hoga
    
main()
    
    