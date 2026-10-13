class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res=[]
        arr1=sorted(arr1)
        hash=Counter(arr1)
        for i in arr2:
            for _ in range(hash[i]):
                res.append(i)
                arr1.remove(i)
        while arr1:
            res.append(arr1.pop(0))
        return res
        