class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {"]": "[", "}" : "{", ")" : "("}
        opening = {"[", "{", "("}
        closing = {"]", "}", ")"}
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack or stack[-1] != paran[i]:
                    return False
                stack.pop()
        return not stack      


        
        