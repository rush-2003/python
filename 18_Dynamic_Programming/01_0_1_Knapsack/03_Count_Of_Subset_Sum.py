# The goal is to determine whether there exists a subset of a given set of integers 
# that adds up to a specific target sum and return the count of these subsets.
# nums = [3, 34, 4, 12, 5, 2]
# target = 9


arr = [2,8,10,12] #Weight,Values,
target = 10 #Capacity

# n=4
# n+1=5
# w=10
# w+1=11

#Making of table t[6][11]
t = [[None for j in range(11)] for i in range(5)]

#initilizaton
for i in range(5):
    for j in range(11):
        if i==0:
            t[i][j] = 0
        if j==0:
            t[i][j] = 1
            

for i in range(1,5):
    for j in range(1,11):
        if arr[i-1] <= j:
            t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
        else:
            t[i][j] = t[i-1][j]

            
print(t[4][10])
        