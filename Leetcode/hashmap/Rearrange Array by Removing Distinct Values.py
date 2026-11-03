class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        hash=Counter(nums)
        res=[]
        max_frequency=max(hash.values())
        unique=sorted(hash.keys())
        for _ in range(max_frequency):
            for value in unique:
                if hash[value]:
                    res.append(value)
                    hash[value]-=1
        return res