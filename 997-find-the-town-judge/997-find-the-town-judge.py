class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        temp1=[0]*(n+1)
        temp2=[0]*(n+1)
        for i in trust:
            temp1[i[0]]+=1
            temp2[i[1]]+=1
        for i in range(1,n+1):
            if temp1[i]==0 and temp2[i]==n-1:
                return i
            
        return -1
        
            