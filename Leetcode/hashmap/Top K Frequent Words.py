from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash=Counter(words)
        strings=sorted(hash.keys(),key=lambda x:(-hash[x],x))
        return strings[:k]