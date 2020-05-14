# Ternary Search

## Divide and conquer method.

### Given sorted array is divided into 3 equal parts and key is comapred to be searched in the part it lies.

```
def ternarySearch(A,x,l,r):
    while(l<=r):
        mid1=l+(r-l)//3
        mid2=mid1+(r-l)//3
        if(x==A[mid1]):
            return mid1
        if(x==A[mid2]):
            return mid2
        if(x<A[mid1]):
            r=mid1-1
        elif(x>A[mid1] and x<A[mid2]):
            l=mid1+1
            r=mid2-1
        else:
            l=mid2+1
    return -1
if __name__=="__main__":
    n=int(input())
    A=list(map(int,input().split()))
    x=int(input())
    p=ternarySearch(A,x,0,n-1)
    if(p>=0):
        print(f"{x} found at position {p+1}")
    else:
        print("Element not found")
    
            
        
                  
```


