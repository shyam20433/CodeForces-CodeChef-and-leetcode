class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2=rec1
        x3,y3,x4,y4=rec2
        width=min(x2,x4)-max(x1,x3)
        height=min(y2,y4)-max(y1,y3)
        return width>0 and height>0       