class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n=len(indices)
        res=[0]*n
        for i in range(len(indices)):
            res[indices[i]]=s[i]
        return "".join(res)
        