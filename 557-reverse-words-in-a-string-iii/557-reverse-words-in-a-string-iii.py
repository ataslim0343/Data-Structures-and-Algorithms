class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        L=[]
        p=""
        for i in l:
            L.append(i[::-1])
        p=" ".join(L)
        return p