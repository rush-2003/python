from random import randint

actual_number = randint(0,100)
print(f"Actual number is {actual_number}")

count = 0

flag = True

while(flag):
    user_guess = int(input("Enter your guess: "))
    count += 1
    if(actual_number > user_guess):
        print("Higher the number please")
    elif(actual_number == user_guess):
        flag=False
        print("Congratulations! your guess is correct")
        print(f"Your number of guess were {count}")
    else:
        print("Lower the number please")
        
print("End of the program")