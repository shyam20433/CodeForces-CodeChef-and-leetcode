n=int(input())
ans=0
for _ in range(n):
    count=0
    a,b,c=list(map(int,input().split()))
    if a==1:
        count+=1
    if b==1:
        count+=1
    if c==1:
        count+=1
    if count>1:
        ans+=1
print(ans)

