a=int(input())
b=int(input())
c=int(input())
d=int(input())
n=int(input())
if a==1:
    print(n)
else:
    count=0
    for i in range(1,n+1):
        if i%a and i%b and i%c and i%d:
            count+=1
    print(n-count)