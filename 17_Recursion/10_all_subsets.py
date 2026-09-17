# We have to print all subsets of an array
# arr = [1, 2,] then subsets are [], [1], [2], [1, 2]

# Here we follow: input output method — Recurssive Tree approach
# Basically we have decision to make, we have choices and we have to make the input smaller

# Recursive tree Structure
'''
                  ip, op
                    /\
    small ip, op1     small in, op2
'''

# How our tree will look
'''
                                        ip=[1, 2], op=[]
                    we will not take 1          /\          we will take 1          Position where we have to take decision for 1
                                               /  \
                              ip=[1,2], op1[]            ip=[2], op2[1]
                                    /\
             we will not take2     /  \   we will take 2                            Position where we have to take decision for 2
             
                                                .
                                                .
                                                .
                 at leaf node our input becomes empty and output is the subset
'''

allSubsets = []
def subsets(ip, op = []):
    if len(ip) == 0:
        allSubsets.append(op[:])
        return
    
    op1 = op[:]
    
    op2 = op[:]
    op2.append(ip[0])
    
    smaller_ip = ip[1:]
    
    subsets(smaller_ip, op1)
    subsets(smaller_ip, op2)
    
    return

subsets([1,2,3])
print(allSubsets)
    