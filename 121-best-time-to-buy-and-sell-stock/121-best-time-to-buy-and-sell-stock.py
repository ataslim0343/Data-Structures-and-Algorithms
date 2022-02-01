class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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