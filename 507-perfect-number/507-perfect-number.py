class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num==1):
            return 0
        s=0
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                s+=i+num//i
        return (s+1==num)
            
        