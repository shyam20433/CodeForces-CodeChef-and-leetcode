t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    left=0
    right=n-1
    target=1
    isPossible=True
    while left<=right:
        if nums[left]==target:
            left+=1
            target+=1
        elif nums[right]==target:
            right-=1
            target+=1
        else:
            isPossible=False
            break
    if isPossible:
        print("YES")
    else:
        print("NO")
