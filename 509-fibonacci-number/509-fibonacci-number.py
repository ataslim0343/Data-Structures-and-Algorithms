class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        s=0
        if(n==1):
            return 1
        for i in range(n-1):
            s=a+b
            a=b
            b=s
        return s
        