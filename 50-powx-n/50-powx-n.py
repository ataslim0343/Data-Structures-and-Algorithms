class Solution(object):
    def myPow(self, x, n):
        # if n==0 or x==1.0:
        #     return 1.0
        # if x==0:
        #     if(n<0):
        #         return float(inf)
        #     else:
        #         return 0.0
        if n<0:
            x=1/x
            n=abs(n)
        res=1
        while(n>0):
            if(n%2==0):
                x=x*x
                n=n//2
            res*=x
            n-=1
        return res
        