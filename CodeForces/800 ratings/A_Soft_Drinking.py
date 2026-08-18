n,k,l,c,d,p,nl,np=list(map(int,input().split()))
milliliters=k*l
toats=milliliters//nl
limes=c*d
salt=p//np
print(min(salt,toats,limes)//n)