// Transpose of a square matrix

void transpose( int A[][N],int n) 
{   int temp;
    for(int i=0;i<n;i++)
    {
        for(int j=i;j<N;j++)
        {
            temp=A[i][j];
            A[i][j]=A[j][i];
            A[j][i]=temp;
        }
    }
}
