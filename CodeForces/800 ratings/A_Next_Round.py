n,k=list(map(int,input().split()))
nums=list(map(int,input().split()))
target=nums[k-1]
count=0
for i in nums:
    if i>=target and i>0:
        count+=1
print(count)
