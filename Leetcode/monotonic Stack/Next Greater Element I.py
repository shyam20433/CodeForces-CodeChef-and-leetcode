from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=defaultdict(lambda:-1)
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and nums2[stack[-1]]<curr:
                res[nums2[stack.pop()]]=curr
            stack.append(i)
        return [res[num] for num in nums1]