class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        n=len(nums)
        #take care of the case where k >= len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]
        