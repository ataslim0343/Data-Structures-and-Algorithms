class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
        # def helper(n):
        #     n=str(n)
        #     for i in range(1,len(n)):
        #         if int(n[i])-int(n[i-1])!=1:
        #             return 0
        #             break
        #     return 1
        # result=[]            
        # for i in range(low,high+1):
        #     if helper(i):
        #         result.append(i)
        # return sorted(result)
        
        s='123456789'
        res=[]
        for i in range(9):
            for j in range(i+1,9):
                temp=int(s[i:j+1])
                if(temp>=low and temp<=high):
                    res.append(temp)
        return sorted(res)