from collections import Counter,groupby
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        nums=[key for key,group in groupby(nums)]
        """
        res=[nums[0]]
        for i in nums[1:]:
            if i!=res[-1]:
                res.append(i) 
        """
        hash=Counter(nums)
        count=0
        for key,value in hash.items():
            if value==1:
                count+=1
        return count