class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        s=ord(coordinates[0])+int(coordinates[1])
        # print(s)
        return s%2
            
        