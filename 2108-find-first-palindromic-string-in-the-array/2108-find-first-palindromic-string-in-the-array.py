class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def isPalindrome(s):
            rev=""
            for i in range(len(s)):
                rev=s[i]+rev
            return rev
        for i in words:
            if isPalindrome(i)==i:
                return i
                break
        return ""
        