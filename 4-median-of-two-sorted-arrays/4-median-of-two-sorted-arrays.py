class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
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
        p=m+n
        print(ans)
        if(p%2==0):
            res=ans[p//2]+ans[(p//2)-1]
            #print(res)
            return res/2.0
        else:
            res=ans[p//2]
            return res