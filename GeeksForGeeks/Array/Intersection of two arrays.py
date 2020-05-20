# Given two arrays a and b respectively of size n and m. The task is to print the count of elements in the 
# intersection (or common elements) of the two arrays.


def countIntersection(a, b, n, m):
    ans=[]
    d={}
    for i in b:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for j in a:
        if j in d and j not in ans:
            ans.append(j)
    return len(ans)
    
for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(countIntersection(a, b, n, m))
