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
            s=s*10+x%10
            x=x//10
        return s==temp
            
        