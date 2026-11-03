class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        res=""
        for i in words:
            res+=i
            if res not in s:
                return False
            if res==s:
                return True
        return False
        