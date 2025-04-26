# 1. What is a Hashmap?
# A hashmap is a data structure that stores key-value pairs. It allows fast access to data using a unique key.

# In Python, the built-in dictionary (dict) is an example of a hashmap.

# 2. How Does a Hashmap Work?
# Every key is passed through a hash function.
# The hash function converts the key into a unique index (hash value).
# This index decides where the value is stored.
# When searching for a key, Python calculates the same index and retrieves the value instantly.

subject_marks = {
    "English" : 80,
    "Marathi" : 75,
    "Hindi" : 90,
    "Immutable and Unique" : "Any Datatype"
}

print(subject_marks)

print(subject_marks['Hindi'])
print(subject_marks['English'])


# 3. What is a Hashtable?
# A hashtable is another name for a hashmap, but the difference is:

# Hashmaps allow multiple threads to access them (not thread-safe).
# Hashtables are thread-safe (used in multi-threaded applications).
# Python's dict is not thread-safe, but we can use thread-safe alternatives like collections.OrderedDict or concurrent.futures.

#Create
subject_marks["History"] = 95
print(subject_marks)

#Read
print(subject_marks["History"])

#Update
subject_marks["English"] = 100
print(subject_marks)

#Delete
del subject_marks["History"]
print(subject_marks)


# 5. Handling Collisions
# Collisions occur when two keys generate the same hash index. Python handles collisions using:

# Chaining: Storing multiple values at the same index using a list.
# Open Addressing: Finding the next available index.
# Python's dict uses chaining internally.


#Get function
print(subject_marks.get("English", "Not Found"))  # Output: Not Found

#Iterating over hashmap
for key, value in subject_marks.items():
    print(f"{key}: {value}")
    
#Key existence in list
if "English" in subject_marks:
    print("Name exists in dictionary")

