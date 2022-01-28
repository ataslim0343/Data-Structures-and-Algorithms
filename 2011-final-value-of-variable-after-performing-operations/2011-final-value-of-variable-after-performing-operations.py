class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for i in operations:
            if i=="++X":
                ans+=1
            if i=="X++":
                ans+=1
            if i=="--X":
                ans-=1
            if i=="X--":
                ans-=1
        return ans
            
        
        