# default mode is read

f = open("08_File_IO/data.txt")
data = f.read()
print(data)
f.close()

var = open('08_File_IO/data.txt', 'w')
st = "Rudalph is 2nd dan karate blackbelt"
var.write(st)
f.close()

var1 = open('08_File_IO/data.txt')
lines = var1.readlines()
print(lines)
var1.close()


var2 = open('08_File_IO/data.txt')
line1 = var2.readline()
print(line1)
line2 = var2.readline()
print(line2)
line3 = var2.readline()
print(line3)
var1.close()


var3 = open('08_File_IO/data.txt', 'a')
strg = "\nRudalph is a good coder"
var3.write(strg)
var3.close()
