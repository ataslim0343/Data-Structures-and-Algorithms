//We can sort the array in 0(nlon) time by quick or merge sort.
//But it is possible to sort the array in 0(n) time.
//Since there are three distinct numbers 0,1 and 2-- 0's will always lie in left, 1's in middle and 2's in right.


void sort012(int a[], int n)
{
    int left,mid,right,temp;
    //maintain 3 pointers, left for 0, mid for 1 and right for 2.
    left=0,mid=0,right=n-1;
    //iterate mid from 0 to n-1.
    while(mid<=right)
    {
        if(a[mid]==0)
        {
            //swap mid element with left bcoz 0 will always lie in left
            temp=a[mid];
            a[mid]=a[left];
            a[left]=temp;
            //increament left and mid by 1.
            left++;
            mid++;
        }
        else if(a[mid]==1)
        {
            //no swappingm bcoz 1 will always lie in middle
            //increament mid by 1.
            mid++;
        }
        else
        {
            //swap mid element with right bcoz 2 will always lie in right
            temp=a[mid];
            a[mid]=a[right];
            a[right]=temp;
            //Decreament right  by 1.
            right--;
            
        }
    }    
}
