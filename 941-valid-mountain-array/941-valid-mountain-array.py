class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        m=max(arr)
        k=arr.index(m)
        n=len(arr)
        if(n==1 or n==2 or k==n-1 or k==0):
            return 0
        f1,f2=0,0
        for i in range(1,k+1):
            if arr[i]-arr[i-1]>=1:
                pass
            else:
                f1=1
        for i in range(k+1,n):
            if arr[i-1]-arr[i]>=1:
                pass
            else:
                f2=1
        if(f1==0 and f2==0):
            return 1
        else:
            return 0