class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        res=""
        for i in s:
            res=i+res
        return res