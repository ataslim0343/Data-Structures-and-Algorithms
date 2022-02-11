class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res=""
        s=sentence.split()
        v=('a', 'e', 'i', 'o','u','I','O','U','A','E')
        for i in range(len(s)):
            if s[i][0] in v:
                res+=s[i]+"ma"+"a"*(i+1)+" "
            else:
                res+=s[i][1:]+s[i][0]+"ma"+"a"*(i+1)+" "
        return res.strip()