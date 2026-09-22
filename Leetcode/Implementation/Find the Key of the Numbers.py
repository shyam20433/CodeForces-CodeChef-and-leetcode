class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def generate(num1):
            return str(num1).zfill(4)
        num1=generate(num1)
        num2=generate(num2)
        num3=generate(num3)
        ans=""
        for i in range(4):
            ans+=min(num1[i],num2[i],num3[i])

        return int(ans)
