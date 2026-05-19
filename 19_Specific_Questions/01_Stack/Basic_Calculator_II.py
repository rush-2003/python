class Solution:
    def calculate(self, s: str) -> int:

        def evaluate(operand1, operand2, operator):
            if operator == "+":
                return operand1 + operand2
            elif operator == "-":
                return operand1 - operand2
            elif operator == "*":
                return operand1 * operand2
            else:
                return operand1 // operand2
        
        def precedence(op):
            if op == "+" or op == "-":
                return 1
            else:
                return 2

        for op in "+-*/":
            s = s.replace(op, f" {op} ")
        arr = s.split()

        operators = []
        operands = []

        for item in arr:
            if item == "+" or item == "-" or item == "*" or item == "/":
                if not operators:
                    operators.append(item)
                else:
                    while operators and precedence(operators[-1]) >= precedence(item):
                        operand2 = operands.pop()
                        operand1 = operands.pop()
                        operator = operators.pop()
                        ans = evaluate(operand1, operand2, operator)
                        operands.append(ans)
                    operators.append(item)

            else:
                operands.append(int(item))

        while operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            operator = operators.pop()
            ans = evaluate(operand1, operand2, operator)
            operands.append(ans)
            
        return operands[0]
    
    
# 1. Evaluate function is easy
# 2. Precedence function is easy
# 3. How to split the string is question dependent. - Brainstroming
# 4. Once split is done we get our exact question array
# 5. We keep 2 stacks - one for operators and one for operands
# 6. We iterate through the array and if we get an operand we push it to the operand stack
# 7. If we get an operator
#    a. If operator stack is empty we push the operator to the stack
#    b. If operator stack is not empty we check the precedence 
#    c. If precedence of the top operator is greater than or equal to the current operator - we evaluate
#    d. We keep evaluating until we get an operator with less precedence than the current operator or the stack is empty
#    e. Finally we push the current operator to the stack
# 8. After iterating through the array we might have some operators left in the stack
# 9. We keep evaluating until the operator stack is empty
# 10. Finally we return the only element left in the operand stack as the answer
