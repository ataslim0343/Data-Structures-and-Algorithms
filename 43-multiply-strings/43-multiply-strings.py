class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        def strToInt(p):
            integer=0
            for i in p:
                integer=(integer*10)+(ord(i)-ord('0'))
            return integer
        
        def intToStr(p):
            s=""
            while(p):
                r=p%10
                p=p//10
                s=chr(ord('0')+r)+s
            return s
            
        return intToStr(strToInt(num1)*strToInt(num2))
    
                
        