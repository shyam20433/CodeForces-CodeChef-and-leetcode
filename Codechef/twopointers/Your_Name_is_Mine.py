# cook your dish here
n=int(input())
for _ in range(n):
    name1,name2=list(map(str,input().split()))
    
    def check(name1,name2):
        i=0
        j=0
        while i<len(name1) and j<len(name2):
            if name1[i]==name2[j]:
                i+=1 
            j+=1
        return i==len(name1)
        
    if check(name1,name2) or check(name2,name1):
        print("YES")
    else:
        print("NO")