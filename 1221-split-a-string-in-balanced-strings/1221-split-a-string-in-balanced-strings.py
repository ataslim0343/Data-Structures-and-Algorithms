class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        l=0
        n=0
        for i in s:
            if i=="R":
                r+=1
            else:
                l+=1
            if(r==l):
                n+=1
        return(n)
        