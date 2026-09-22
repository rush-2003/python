# We are given a String - lets say "ab"
# We are suppose to generate following of the given string
'''
ab
Ab
aB
AB
'''
# Note every character is given a chance to be in uppercase and lowercase
# We will follow ip-op recursive tree approach

'''
                                        ip=[a, b], op = []
                                                  /\
                  'a' can be in lowercase        /  \      'a' can be in uppercase
                                 ip=[b], op=[a]       ip=[b], op=[A]
                                                  .
                                                  .
                                      Now take decision for 'b'
'''


def permutation_with_case_change(ip, op):
    if len(ip) == 0:
        print("".join(op))
        return
    
    op1 = op[:]
    op1.append(ip[0])
    
    op2 = op[:]
    op2.append(ip[0].upper())
    
    smaller_ip = ip[1:]
    
    permutation_with_case_change(smaller_ip, op1)
    permutation_with_case_change(smaller_ip, op2)
    
    return

ip = ['a', 'b']
op = []
permutation_with_case_change(ip, op)