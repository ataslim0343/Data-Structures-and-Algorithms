# Intersection of two sorted array if we need to print duplicate intersection elements as well.

```
def printIntersection(a, b, n, m):
    newArray=[]
    i=j=0
    while(i<n and j<m):
        if(a[i]<b[j]):
            i+=1
        elif(a[i]>b[j]):
            j+=1
        else:
            newArray.append(a[i])
            i+=1
            j+=1
    for i in newArray:
        print(i,end=" ")
```
