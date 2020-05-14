# Binary Search - Recursive Approach

```
def binSearch(A,x,l,r):
    if(l<=r):
        mid= l+(r-l)//2
        if(A[mid]==x):
            return 1
        elif(A[mid]>x):
            return binSearch(A,x,l,mid-1)
        else:
            return binSearch(A,x,mid+1,r)
    else:
        return -1

def main():
    for i in range(int(input())):
        n,x=map(int,input().split())
        A=[int(i) for i in input().split()]
        print(binSearch(A,x,0,n-1))
if __name__=="__main__":
    main()
    
 ```
 
 
 # Binary Search - Iterative Approach
 
 
 ```
 
 def bin_search(arr, left, high, key):
    high=len(arr)-1
    while(left<=high):
        mid=left+(high-left)//2
        if(arr[mid]==key):
            return mid
        if(key>arr[mid]):
            left=mid+1
        if(key<arr[mid]):
            high=mid-1
    return -1
    
  ```
 
 
