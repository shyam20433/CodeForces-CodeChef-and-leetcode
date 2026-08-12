n=int(input())
for i in range(n):
    n,target=list(map(int,input().split()))
    nums=sorted(list(map(int,input().split())))
    count=0
    left=0
    right=1
    while left<n and right<n:
        if right!=left and abs(nums[left]-nums[right])==target:
            count=1
            break
        elif abs(nums[left]-nums[right])<target:
            right+=1
        else:
            left+=1
    print(count)
