# cook your dish here
t=int(input())
for _ in range(t):
    total=0
    n=int(input())
    while n:
        if n>1:
            total+=30
            n-=2
        else:
            total+=20
            n-=1
    print(total)