class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def isLower(s):
            c_lower=0
            for i in s:
                if ord(i)>=97 and ord(i)<=122:
                    c_lower+=1
            n=len(s)
            if(n==c_lower):
                return 1
            return 0

        def isUpper(s):
            c_upper=0
            for i in s:
                if ord(i)>=65 and ord(i)<=90:
                    c_upper+=1
            n=len(s)
            if(n==c_upper):
                return 1
            return 0
        
        
        if(isUpper(word) or isLower(word) or (isUpper(word[0]) and isLower(word[1:]))):
            return 1
        else:
            return 0
        