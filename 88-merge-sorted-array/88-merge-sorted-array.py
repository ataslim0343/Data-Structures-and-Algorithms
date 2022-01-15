class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans=[0]*(m+n)
        i,j,k=0,0,0
        while(i<m and j<n):
            if(nums1[i]<=nums2[j]):
                ans[k]=nums1[i]
                k+=1
                i+=1
            else:
                ans[k]=nums2[j]
                k+=1
                j+=1
        while(i<m):
            ans[k]=nums1[i]
            k+=1
            i+=1
        while(j<n):
            ans[k]=nums2[j]
            k+=1
            j+=1
        for i in range(m+n):
            nums1[i]=ans[i]