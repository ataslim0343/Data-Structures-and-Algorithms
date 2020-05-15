# Peak Element

## Problem statement 

### C++ Solution - (0.01 Sec)

Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
Note: There may be multiple peak element possible, in that case you may return any valid index.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N. Then in the next line are N space separated values of the array.

Output:
For each test case output will be 1 if the index returned by the function is an index with peak element.

User Task:
You don't have to take any input. Just complete the provided function peakElement() and return the valid index.

Constraints:<br>
1 <= T <= 100<br>
1 <= N <= 105<br>
1 <= A[] <= 106<br>

Example:<br>
Input:<br>
2<br>
3<br>
1 2 3<br>
2<br>
3 4<br>
Output:<br>
1<br>
1<br>

Explanation:<br>
Testcase 1: In the given array, 3 is the peak element as it is greater than its neighbour.<br>
Testcase 2: 4 is the peak element as it is greater than its neighbour elements.<br>


```
int peakElement(int arr[], int n)
{
   int l,h,mid;
   l=0;
   h=n-1;
   while(l<=h){
       mid=l+(h-l)/2;
       //Checking from 1 to second last element, avoiding boundry condition here.
       if(mid>0 && mid<n-1){
           if(arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]){
               return mid;
           }
           else if(arr[mid-1]>arr[mid]){
               h=mid-1;
           }
            else{
                l=mid+1;
            }
       }
       //From here we will be dealing with boundary conditions.
       //Left Boundry
       else if(mid==0){
           if(arr[0]>arr[1]){
               return 0;
           }
           else{
               return 1;
           }
       }
       //Right Boundry
       else if(mid==n-1){
           if(arr[mid]>arr[mid-1]){
               return mid;
           }
           else{
               return mid-1;
           }
       }
           
   }
   return 0;
}







```
