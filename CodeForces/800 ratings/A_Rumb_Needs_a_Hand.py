t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    mis=[]
    for i in range(n):
        if nums[i]!=i+1:
            mis.append(nums[i])
    isPossible=True
    for i in range(len(mis)-1):
        if mis[i]<mis[i+1]:
            isPossible=False
            break
    if isPossible:
        print("YES")
    else:
        print("NO")