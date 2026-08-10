n=int(input())
for i in range(n):
    nums=sorted(list(map(int,input().split())))
    count=0
    while True:
      if nums[0]==nums[1] or nums[1]==nums[2]:
          break
      nums[2]-=1
      nums[0]+=1
      count+=1
      nums.sort()
    print(count)


