n=int(input())
nums=list(map(int,input().split()))
count=0
maxi=nums[0]
mini=nums[0]

for i in range(1,len(nums)):
    if nums[i]>maxi:
        count+=1
        maxi=nums[i]
    elif nums[i]<mini:
        count+=1
        mini=nums[i]
print(count)