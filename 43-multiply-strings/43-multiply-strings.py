class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def strToInt(p):
            integer=0
            for i in p:
                integer=(integer*10)+(ord(i)-ord('0'))
            return integer
        return str(strToInt(num1)*strToInt(num2))
    
                
        