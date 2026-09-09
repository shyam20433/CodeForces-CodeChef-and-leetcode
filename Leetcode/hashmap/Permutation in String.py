class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        word1=[0]*26
        for i in s1:
            word1[ord(i)-ord('a')]+=1
        for i in range(len(s2)-len(s1)+1):
            word2=[0]*26
            sub=s2[i:i+len(s1)]
            for c in sub:
                word2[ord(c)-ord('a')]+=1
            if word1==word2:
                return True
        return False