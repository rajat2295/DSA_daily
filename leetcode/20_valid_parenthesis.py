class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for bracket in s:
            if bracket == '[' or bracket == '{' or bracket == '(':
                stack.append(bracket)
            elif len(stack) and bracket is ')' and stack[-1] =='(':
                stack.pop()
            elif len(stack) and bracket is ']' and stack[-1] =='[':
                stack.pop()
            elif len(stack) and bracket is '}' and stack[-1] =='{':
                stack.pop()
            else:
                return False
        return len(stack) == 0
            
                 
