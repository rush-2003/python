# Given an array arr[], determine if it can be partitioned into two subsets such that 
# the sum of elements in both parts is the same.

'''
Logic:
its only possible if sum of given array is even
if odd then its not possible
'''

'''
So basically what we do is
1. We calculate the sum of all the elements of array
2. If its even we proceed else return False
3. Now the array is given arr = [.......]
4. And target is sum/2 target = sum(arr)/2
5. Now use Subset_Sum_Problem logic
'''
