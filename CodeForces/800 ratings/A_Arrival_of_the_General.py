n=int(input())
nums=list(map(int,input().split()))
count=0
max_index=nums.index(max(nums))
min_index=len(nums)-1-nums[::-1].index(min(nums))
if min_index<max_index:
    count-=1
count+=max_index+n-1-min_index
print(count)