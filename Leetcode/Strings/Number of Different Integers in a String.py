class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen=set()
        number=""
        for i in word:
            if i.isdigit():
                number+=i
            else:
                if number:
                    seen.add(int(number))
                number=""
            print(seen)
        if number:
            seen.add(int(number))
        return len(seen)
        