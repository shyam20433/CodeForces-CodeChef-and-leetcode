import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph=re.sub(r'[^\w\s]', ' ', paragraph).lower()
        hash=Counter(paragraph.split())
        print(hash)
        for word in banned:
            if word in hash:
                hash.pop(word)
        hash=list(sorted(hash.items(),key=lambda x:x[-1],reverse=True))
        return hash[0][0]