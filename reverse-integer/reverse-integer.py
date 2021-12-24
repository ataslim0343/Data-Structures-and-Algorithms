class Solution:
    def reverse(self, x: int) -> int:
        s=0
        n=x
        
        if(x<0):
            n=n*-1
        while(n>0):
            r=n%10
            n=n//10
            s=s*10+r
        if -2**31 <= s <= (2**31)-1:
            if(x<0):
                return "-"+str(s)
            else:
                return s
        else:
            return 0