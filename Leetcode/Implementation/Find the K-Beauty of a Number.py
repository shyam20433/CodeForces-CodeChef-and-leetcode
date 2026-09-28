class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        original=num
        num=str(num)
        count=0
        for i in range(len(num)-k+1):
            sub=int(num[i:i+k])
            if sub>0 and original%sub==0:
                count+=1
        return count