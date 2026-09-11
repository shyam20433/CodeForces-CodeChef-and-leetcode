n=int(input())

lucky=0
while n:
    rem=n%10
    if rem==4 or rem==7:
        lucky+=1
    n//=10
if lucky==4 or lucky==7:
    print("YES")
else:
    print("NO")