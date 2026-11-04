n=int(input())
nums=list(map(int,input().split()))
neg=[]
pos=[]
zero=[]
for i in nums:
    if i<0:
        neg.append(i)
    elif i>0:
        pos.append(i)
    else:
        zero.append(i)

set1=[]
set2=[]
set3=[]

set1.append(neg.pop())
if pos:
    set2.extend(pos)
else:
    set2.append(neg.pop())
    set2.append(neg.pop())

set3+=neg+zero
print(len(set1),*set1)
print(len(set2),*set2)
print(len(set3),*set3)


