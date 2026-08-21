class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split("/")
        for word in path:
            if stack and word=="..":
                stack.pop()
            elif word not in [".","",".."]:
                stack.append(word)
        return "/"+"/".join(stack)

       