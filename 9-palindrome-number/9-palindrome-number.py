class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        s=0
        if(x<0):
            return False
        while(x):
            r=x%10
            x=x//10
            s=s*10+r
        return s==temp
            
        