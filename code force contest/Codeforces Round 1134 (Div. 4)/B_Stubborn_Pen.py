t=int(input())
for _ in range(t):
    n=int(input())
    color=str(input())
    count=0
    if color[0]!="R":
        count+=1
    for i in range(1,n):
        if color[i]==color[i-1]:
            count+=1
    print(count)