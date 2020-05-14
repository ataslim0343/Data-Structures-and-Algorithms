# Sqaure root using Binary Search
## C++ Solution

### Example:
Input:
2<br>
5<br>
4<br>
Output:<br>
2<br>
2<br>

Explanation:
Testcase 1: Since, 5 is not perfect square, so floor of square_root of 5 is 2.<br>
Testcase 2: Since, 4 is a perfect square, so its square root is 2.<br>



```
long long int floorSqrt(long long int x) 
{
    long long int l=1;
    long long int r=x/2;
    long long int mid;
    long long int SQRT;
    if(x==0 ||x==1){
        return x;
    }
    while(l<=r)
    {
        mid=l+(r-l)/2;
        if(mid*mid==x){
            return mid;
        }
        else if(mid*mid<x){
            l=mid+1;
            SQRT=mid;
        }
        else{
            r=mid-1;
        }
    }
    return SQRT;
}

```
