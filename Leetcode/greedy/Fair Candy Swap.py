class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)
        difference=(sumB-sumA)//2
        bobSizes=set(bobSizes)
        for a in aliceSizes:
            if a+difference in bobSizes:
                return [a,a+difference]