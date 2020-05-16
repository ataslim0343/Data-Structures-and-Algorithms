# Search in a Sorted and Rotated Array/Search element in a circular sorted array

## Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.

### Input:<br>
The first line of the input contains an integer T, denoting the total number of test cases. Then T test cases follow. Each test case consists of three lines. The first line of each test case contains an integer N denoting the size of the given array. The second line of each test case contains N space-separated integers denoting the elements of the array A. The third line of each test case contains an integer K denoting the element to be searched in the array.

### Output:<br>
For each test case, print the index of the element K in a new line, if K does not exist in the array then print -1.

User Task:<br>
Complete Search() function and return the index of the element K if found in the array. If the element is not present, then return -1.

Constraints:<br>
1 ≤ T ≤ 100<br>
1 ≤ N ≤ 107<br>
0 ≤ Ai ≤ 108<br>
1 ≤ K ≤ 108<br>

Example:<br>
Input:<br>
3<br>
9<br>
5 6 7 8 9 10 1 2 3<br>
10<br>
3<br>
3 1 2<br>
1<br>
4<br>
3 5 1 2<br>
6<br>

Output:<br>
5<br>
1<br>
-1<br>

Explanation:<br>
Testcase 1: 10 is found at index 5.


## C++ Solution using Binary Search.

```

int Search(vector<int> vec, int K) {
    int l,h,mid;
    int n=vec.size();
    l=0;
    h=n-1;
    while(l<=h)
    {
        mid=l+(h-l)/2;
        if(vec[mid]==K)
        {
            return mid;
        }
        
        if(vec[mid]<=vec[h]) //Right half is sorted
        {
            if(K>=vec[mid] && K<=vec[h])
            {
                l=mid+1;
            }
            else
            {
                h=mid-1;
            }
        }
        else //Left half is sorted
        {
            if(K>=vec[l] && K<=vec[mid])
            {
                h=mid-1;
            }
            else
            {
                l=mid+1;
            }
        }
    }
    return -1;
}

```
