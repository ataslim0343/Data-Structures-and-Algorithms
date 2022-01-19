class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice=9999999
        maxProfit=0
#         for i in prices:
#             minPrice=min(minPrice,i)
#             maxProfit=max(maxProfit,i-minPrice)
#         return maxProfit
            
        for i in prices:
            if(i<minPrice):
                minPrice=i
            if(maxProfit<i-minPrice):
                maxProfit=i-minPrice
        return maxProfit
        