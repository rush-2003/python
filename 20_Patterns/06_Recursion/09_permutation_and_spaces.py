# We are given a string lets say "ABC"
# Our tasks is to generate permutations
# But while generating the permutations we have to add spaces

'''
For Example String: ABC
We have to generate following permutations
ABC
A_BC
AB_C
A_B_C
'''

# Notice: There are spaces only in between and not in start and end
# What choice we have:
# Either take the letter as it is like A, B, C or take it with space _B, _C
# Its clear that we cant take _A and C_

'''
We will follow Ip-Op Recurssive tree approach
How the recursive tree would look?

                                                ip=[BC], op=[A]
                                B with space _B        /\        B without space B
                                                      /  \
                                    ip=[C], op=[A_B]       ip=[C], op=[AB]
'''

def permutation_with_spaces(ip, op):
    if len(ip) == 0:
        print(''.join(op))
        return

    ch = ip[0]
    remaining_ip = ip[1:]

    # Choice 1: space + character
    op1 = op[:]
    op1.append('_')
    op1.append(ch)

    # Choice 2: character without space
    op2 = op[:]
    op2.append(ch)

    permutation_with_spaces(remaining_ip, op1)
    permutation_with_spaces(remaining_ip, op2)


ip = ['B', 'C']
op = ['A']

permutation_with_spaces(ip, op)