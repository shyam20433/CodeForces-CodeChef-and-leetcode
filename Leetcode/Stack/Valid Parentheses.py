class Solution:
    def isValid(self, s: str) -> bool:
        hash={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i not in hash:
                stack.append(i)
            elif not stack or stack.pop()!=hash[i]:
                return False
        return not stack
        