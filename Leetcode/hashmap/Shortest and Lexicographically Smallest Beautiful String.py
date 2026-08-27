from collections import defaultdict
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1')<k:
            return ""
        hash=defaultdict(int)
        left=0
        res=""
        mini=len(s)+1
        for i in range(len(s)):
            hash[s[i]]+=1
            while hash["1"]>=k:
                length=i-left+1
                subs=s[left:i+1]
                if length<mini:
                    mini=length
                    res=subs
                elif length==mini and subs<res:
                    res=subs

                hash[s[left]]-=1
                if hash[s[left]]==0:
                    hash.pop(s[left])
                left+=1
                
        return res
        