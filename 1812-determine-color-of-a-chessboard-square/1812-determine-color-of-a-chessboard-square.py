class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        g1={'a','c','e','g'}
        g2={'b','d','f','h'}
        
        s=ord(coordinates[0])+int(coordinates[1])
        # print(s)
        return s%2
            
        