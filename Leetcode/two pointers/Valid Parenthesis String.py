class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open=max_open=0
        for i in s:
            if i=="(":
                min_open+=1
                max_open+=1
            elif i==")":
                min_open-=1
                max_open-=1
            elif i=="*":
                min_open-=1 # * => )
                max_open+=1 # * => (
            if max_open<0:
                return False # if ) to many means that not valid
            
            if min_open<0:
                min_open=0
        return min_open==0