# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    hash=Counter(nums)
    count=0
    maxi=max(hash.values())
    for k,v in hash.items():
        if maxi==v:
            count+=1
    if count==1:
        print("YES")
    else:
        print("NO")
        
    