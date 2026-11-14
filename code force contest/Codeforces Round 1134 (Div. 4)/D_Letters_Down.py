t = int(input())
for _ in range(t):
    n = int(input())
    word = list(input().strip())
    count = 0
    while word!=word[::-1]:
        count+=1
        left=0
        right=n-1
        while left<right and word[left]==word[right]:
            
            left+=1
            right-=1
        maxi="a"
        for i in range(left,right+1):
            if word[i]!=word[n-i-1] and word[i]>maxi:maxi=word[i]
        for i in range(n):
            if word[i]==maxi:
                val=(ord(word[i]) - ord('a') - 1) % 26 + ord('a')
                word[i]=chr(val)
    print(count)
            

