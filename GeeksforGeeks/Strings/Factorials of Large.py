class Solution:
    def factorial(self, n):
        product=1
        for i in range(2,n+1):
            product*=i
        nums=[]
        while product:
            nums.append(product%10)
            product//=10
        return nums[::-1]