# Ternary Search

## Divide and conquer method.

### Given sorted array is divided into 3 equal parts and key is comapred to be searched in the part it lies.

```
def fourSum(A,n,X):
    A.sort()
    res=0
    for i in range(n):
        for j in range(i+1,n-2):
            k=j+1
            l=n-1
            while(k<l):
                if A[i]+A[j]+A[k]+A[l]==X:
                    res+=1
                elif A[i]+A[j]+A[k]+A[l]>X:
                    l-=1
                else:
                    k+=1
    print(res if res>0 else -1)
    
for i in range(int(input())):
    n=int(input())
    A=[int(i) for i in input().split()]
    X=int(input())
    fourSum(A,n,X)            
            
            
```


