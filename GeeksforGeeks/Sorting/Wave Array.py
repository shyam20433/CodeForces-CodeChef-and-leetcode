class Solution:
    def sortInWave(self, arr):
        # code here
        end=len(arr)-len(arr)%2
        arr[0:end:2],arr[1:end:2]=arr[1:end:2],arr[0:end:2]
        return arr
