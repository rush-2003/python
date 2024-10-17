name = "Rudalph"

#seedhi ginit 0,1,...
#ulti ginti -1,-2....

slice_string = name[0:3]
print(slice_string)
#variable = string_variable-name[start_index : end_index]
#start_index included
#end_index not included


#Directly using index of the string
print(name[-7])

#Very very important - Negative Slicing
#Likha ulta hai lekin print seedha hota hai
sl = name[-4:-1]
print(sl)

#Start aur end mention nahi kiya hota hai
print(name[:7])
print(name[0:])

#skipping in slicing
#Every xth element will be printed from the previously printed element
x = "rudalphgonsalves"
print(x[0:20:3])
