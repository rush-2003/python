# Replace dummy.txt with  08_File_IO/dummy.txt


# with open('dummy.txt') as f:
#     line = f.readline()
#     while(line != ""):
#         words = line.split()
#         print(words)
#         print(type(words))
#         for item in words:  
#             if(item == "twinkle"):
#                 print("Yes the file contains twinkle word")
#         line = f.readline()

# import random
# def game():
#     x = random.randint(1,100)
#     print("Random Number: ",x)
#     with open('dummy.txt') as f:
#         score = f.read()
#         print("score: " ,score)
#         score = int(score) if score else 0
#         print(score)
#         if(x>score):
#             f1 = open('dummy.txt', 'w')
#             f1.write(str(x))
#             print("New score!")
        
# print("Play the game")
# game() 


# for i in range(1, 11):
#     table_line = f"2 x {i} = {2*i}"
#     with open('dummy.txt','a') as f:
#         if(i==1):
#             f.write(f"{table_line}")
#         else:
#             f.write(f"\n{table_line}")


# f = open('dummy.txt')
# content = f.readlines()
# print(content)
# count = 0
# for item in content:
#     new = ''
#     for word in item.split():
#         var=word
#         if(var=='donkey'):
#             var="#####"
#         new = new +' '+ var
#     content[count] = f"{new.strip()}\n"
#     count = count + 1
    
# print(content)
# f1 = open('dummy.txt', 'w')
# for item in content:
#     f1.write(item)
    
# f1.close()
    
    
# f = open('dummy.txt')
# line = f.readline()
# count = 1
# while line != "":
#     if 'python' in line:
#         print(count)
#     count += 1
#     line = f.readline()
        


        

