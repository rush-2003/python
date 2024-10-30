f = open('08_File_IO/data.txt')
print(f.read())
f.close()

#When we use 'With' Statement we do not have to explicitily close the file

with open('08_File_IO/data.txt') as f:
    print(f.read())
    
print("File closed")