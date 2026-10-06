class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        extra=0
        for i in s:
            if i=="(":
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    extra+=1
        return count+extra