class Solution:
    def convertToTitle(self, num: int) -> str:
        res=[]
        while num>0:
            num-=1
            rem=num%26
            res.append(chr(65+rem))
            num//=26
        return "".join(res[::-1])

        """ res=""
        while num>0:
            num-=1
            rem=num%26
            res=chr(65+rem)+res
            num//=26
        return res """