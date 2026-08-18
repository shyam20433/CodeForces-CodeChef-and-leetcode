n=int(input())
num=str(input())
isLucky=True
for i in num:
    if i=="4" or i=="7":
        continue
    isLucky=False
if  isLucky==False:
    print("NO")
else:
    half1=0
    half2=0
    left=0
    right=n-1
    while left<right:
        half1+=int(num[left])
        half2+=int(num[right])
        left+=1
        right-=1
    if half2==half1:
        print("YES")
    else:
        print("NO")