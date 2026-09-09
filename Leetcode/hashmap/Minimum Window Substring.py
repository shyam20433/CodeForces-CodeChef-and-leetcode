from collections import defaultdict,Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_1=defaultdict(int)
        hash_2=Counter(t)
        left=0
        res=""
        for right in range(len(s)):
            hash_1[s[right]]+=1

            while all(k in hash_1 and hash_1[k]>=v for k,v in hash_2.items()):
                sub=s[left:right+1]
                if not res:
                    res=sub
                if len(sub)<len(res):
                    res=sub
                hash_1[s[left]]-=1
                if hash_1[s[left]]==0:
                    hash_1.pop(s[left])
                left+=1
        return res