#link ~ https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_index=[(num,i) for i,num in enumerate(nums)]
        nums_index.sort(key=lambda x:-x[0])
        top_k=sorted(nums_index[:k],key=lambda x:x[1])
        return [k for k,v in top_k]