/*Given an integer an N. The task is to print the position of first set bit found from right 
side in the binary representation of the number.*/

unsigned int getFirstSetBit(int n){
    
    int k=32;
    int i=0;
    while(n)
    {
        if((n>>i)&1==1)
        {
           return i+1; 
        }
        else
        {
            i+=1;
        }
    }
