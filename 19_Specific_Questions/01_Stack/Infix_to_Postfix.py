def precedence(char):
    if char == '+' or char == '-':
        return 1
    else:
        return 2

infix = "(A+B)*C"
#Expected postfix = A B + C *

stack = []
ans = []

for i in infix:
    if i=='A' or i=='B' or i=='C':
        ans.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    else:
        while stack and precedence(i) <= precedence(stack[-1]):
            if stack[-1] == '(':
                break
            ans.append(stack.pop())
        stack.append(i)
        
while stack:
    ans.append(stack.pop())
        
print(ans)