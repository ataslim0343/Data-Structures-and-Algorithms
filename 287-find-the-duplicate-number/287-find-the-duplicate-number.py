class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # When array is immutable
        # n=len(nums)
        # for i in range(n):
        #     j=abs(nums[i])
        #     if(nums[j]<0):
        #         return j
        #     else:
        #         nums[j]*=-1
        
        s_all=sum(nums)
        n_arr=len(nums)
        s_unique=sum(set(nums))
        n_set=len(set(nums))
        return (s_all-s_unique)//(n_arr-n_set)
        
        
                
            
        
        