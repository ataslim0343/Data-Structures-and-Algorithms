class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        res=[]
        for i in sentences:
            res.append(len(i.split()))
        return max(res)
        