class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = set(['+', '*', '/', '-'])
        operand2 = {'+':lambda x, y: x+y,'-':lambda x,y: x-y, '*':lambda x,y:x*y, '/':lambda x,y:int(x/y)}
        stack=[]
        tokens = list(reversed(tokens))

        while tokens:
            ele = tokens.pop()
            if ele in operand:
                y, x = stack.pop(), stack.pop()
                stack.append(operand2[ele](x, y))
            else:
                stack.append(int(ele))

        return stack[0]