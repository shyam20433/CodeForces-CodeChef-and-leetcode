n,k=list(map(int,input().split()))
books=list(map(int,input().split()))
maxi=0
left=0
total=0
for right in range(n):
    total+=books[right]
    while total>k:
        total-=books[left]
        left+=1
    maxi=max(maxi,right-left+1)
print(maxi)
