class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        stack=[]
        for i in range(len(intervals)):
            if not stack or (intervals[i][0]>stack[-1][0] and intervals[i][0]>stack[-1][-1]):
                stack.append(intervals[i])
            else:
                stack[-1][-1]=max(stack[-1][-1],intervals[i][-1])
        return stack
        