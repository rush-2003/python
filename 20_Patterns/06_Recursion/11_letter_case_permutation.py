# We are given a string with letters and numbers
# For example: a1b2
# We have to do permutation with case change
# But only for alphabets and not for digits

'''
a1b2
A1b2
a1B2
A1B2
'''

# We will follow Ip-Op Recurssive tree approach
'''
                                        ip=[a,1,b,2], op=[]
                                                  /\
                          a with small case      /  \      a with upper case
                         ip=[1, b, 2], op=[a]                 ip=[1, b, 2], op=[A]
                                |                                      |
its 1 (digit) so no case change |                                      |
                                |                                    ......
                        ip=[b, 2], op=[a, 1]                           /\
                                /\
        b with small case      /  \      b with upper case
        ip=[2], op=[a, 1, b]           ip=[2], op=[A, 1, B]
                                  
'''

def letter_case_permutation(ip, op):
    if len(ip) == 0:
        print("".join(op))
        return
    
    if ip[0].isalpha():
        op1 = op[:]
        op2 = op[:]
        
        op1.append(ip[0].lower())
        op2.append(ip[0].upper())
        
        smaller_input = ip[1:]
        
        letter_case_permutation(smaller_input, op1)
        letter_case_permutation(smaller_input, op2)
    else:
        op1 = op[:]
        op1.append(ip[0])
        smaller_input = ip[1:]
        letter_case_permutation(smaller_input, op1)
        
ip = ['a', '1', 'b', '2']
op = []
letter_case_permutation(ip, op)

