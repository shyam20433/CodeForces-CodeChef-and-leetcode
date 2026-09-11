n=int(input())
maxi=0
count=0
for i in range(n):
    exit,enter=list(map(int,input().split()))
    count=count+enter-exit 
    maxi=max(maxi,count)
print(maxi)