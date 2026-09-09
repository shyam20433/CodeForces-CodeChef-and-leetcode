import sys
sys.set_int_max_str_digits(20000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp=[]
        for i in num:
            temp.append(str(i))
        number="".join(temp)
        res=int(number)+k
        result=[]
        for i in str(res):
            result.append(int(i))
        return result