class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence=sentence.split()
        vowels="aeiouAEIOU"
        extra="a"
        res=""
        for word in sentence:
            if word[0] in vowels:
                res+=word
            else:
                res+=word[1:]+word[0]
            res+="ma"+extra
            extra+="a"
            res+=" "
        return res.strip()