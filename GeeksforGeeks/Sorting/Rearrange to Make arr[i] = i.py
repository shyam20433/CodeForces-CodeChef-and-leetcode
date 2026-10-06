class Solution:
    def modifyArray(self, arr):
        i=0
        while i<len(arr):
            if arr[i]!=-1 and arr[i]!=arr[arr[i]]:
                # arr[i],arr[arr[i]]=arr[arr[i]],arr[i]
                temp=arr[i]
                arr[i]=arr[temp]
                arr[temp]=temp
            else:
                i+=1
        return arr