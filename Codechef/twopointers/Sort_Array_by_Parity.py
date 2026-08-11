def sortArrayByParity(nums):
    res=[0]*(len(nums))
    #nums.sort()
    # Write your code here
    left=0
    right=len(nums)-1
    for i in range(len(nums)):
        if nums[i]%2==1:
            res[left]=nums[i]
            left+=1 
        else:
            res[right]=nums[i]
            right-=1 
    res[left:]=res[left:][::-1]
    
    for i in range(len(nums)):
        nums[i]=res[i]
    return nums

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    sortArrayByParity(nums)

    print(" ".join(map(str, nums)))