n=int(input())
duration=list(map(int,input().split()))
a,b=list(map(int,input().split()))
print(sum(duration[a-1:b-1]))