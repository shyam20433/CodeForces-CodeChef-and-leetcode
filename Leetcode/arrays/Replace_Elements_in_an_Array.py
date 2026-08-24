class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictionary={num:i for i,num in enumerate(nums)}
        for old,new in operations:
            index=dictionary[old]
            nums[index]=new
            dictionary[new]=index
        return nums