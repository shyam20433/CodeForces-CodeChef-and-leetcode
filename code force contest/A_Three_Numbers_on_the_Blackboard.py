n=int(input())
for i in range(n):
    a,b,c=sorted(list(map(int,input().split())))
    if a+b<c:
        c=a+b
    print(c-a)