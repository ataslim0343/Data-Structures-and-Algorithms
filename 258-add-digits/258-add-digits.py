class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        while(num):
            if(num>=1 and num<=9):
                return num
            s=0
            while(num):
                r=num%10
                num=num//10
                s+=r
            num=s
        return s
                
            
            
            
            
        