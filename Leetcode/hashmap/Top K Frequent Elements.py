from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash=Counter(nums)
        hash=dict(sorted(hash.items(),key=lambda x:x[-1],reverse=True))
        return list(hash.keys())[:k]