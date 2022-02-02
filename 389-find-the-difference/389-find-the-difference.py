class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=0
        # for i in s:
        #     c=c^ord(i)
        # for j in t:
        #     c=c^ord(j)
        # return chr(c)
        
        for i in range(len(s)):
            x+=ord(t[i])
            x-=ord(s[i])
        x+=ord(t[-1])
        return chr(x)
            
            
            
        
        