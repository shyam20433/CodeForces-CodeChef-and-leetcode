n=int(input())
nums=list(map(int,input().split()))
left,right=1,len(nums)
mini=abs(nums[0]-nums[-1])
for i in range(1,len(nums)):
    if abs(nums[i]-nums[i-1])<mini:
        mini=abs(nums[i]-nums[i-1])
        left,right=i+1,i-1+1
print(right,left)
    
