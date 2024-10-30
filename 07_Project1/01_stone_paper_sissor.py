import random
import pyjokes
import pyquotegen

def calculation(value):
    entities = ["stone", "paper", "sissor"]
    computer_choice = random.choice(entities)
    print("Your choice: ", value)
    print("computer choice: ", computer_choice)
    if(value==computer_choice):
        return "Tie"
    elif(value == "stone" and computer_choice=="paper"):
        return "computer won"
    elif(value == "paper" and computer_choice == "stone"):
        return "you won"
    elif(value == "paper" and computer_choice == "sissor"):
        return "computer won"
    elif(value == "sissor" and computer_choice == "paper"):
        return "you won"
    elif(value == "stone" and computer_choice == "sissor"):
        return "you won"
    elif(value == "sissor" and computer_choice == "stone"):
        return "computer won"


name  = input("Enter your name: \n")


print(f'''Hello {name} \n,
Select 1 for stone
Select 2 for paper
Select 3 for sissor\n\n
If you won I tell you a joke 🤯 
''')

user_choice = int(input("Enter your choice: \n"))
result = None
x = None
match user_choice:
    case 1:
        x="stone"
        result = calculation(x)
        print(result)
    case 2:
        x="paper"
        result = calculation(x)
        print(result)
    case 3:
        x="sissor"
        result = calculation(x)
        print(result)
    case _ :
        print("In Valid input")
        
flag = False   
if(result == "Tie"):
    print(f"Hey {name}, its a ite \n")
elif(result.startswith("you")):
    print(f"congratulations! {name}, you won \n")
    flag = True
else:
    print(f"oops! {name}, you lost \n")
    

if(flag==True):
    print("Joke..")
    print(pyjokes.get_joke())
else:
    print(f"Get motivated {name}")
    quote_by_category = pyquotegen.get_quote("motivational")
    print(quote_by_category)
    
    
        
    

