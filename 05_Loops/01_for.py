for i in range(1,6):
    print(i)

#STEP     
for i in range(1, 10, 4):
    print(i)
    
stri = "Rudalph Gonsalves"
for i in stri:
    print(i)
    
l = ["Rudalph", "Gonsalves"]
for i in l:
    print(i)
    
t = (123, 248, "Rudalph")
for i in t:
    print(i)
    
# For with else
# If for loop is not terminated by break statement then else block will be executed
lists = ["I", "am", "good", "boy"]
for i in lists:
    print(i)
else:
    print("For loop with else conditional statement")