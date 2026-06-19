from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=('+','-','*','/')
        stack=deque()
        for i in tokens:
            if i in s:
                r=stack.pop()
                l=stack.pop()
                if i=='+':
                    stack.append(l+r)
                elif i=='-':
                    stack.append(l-r)
                elif i=='*':
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))
            else:
                stack.append(int(i))
        return stack[-1]
