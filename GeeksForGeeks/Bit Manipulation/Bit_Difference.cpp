/* You are given two numbers A and B. 
Write a program to count number of bits needed to be flipped to convert A to B.*/

//Code

int countBitsFlip(int a, int b){
    
    //idea is to find the XOR of a and b and then count set bits.
    int k,count=0;
    k=a^b;
    while(k)
    {
        count+=1;
        k=k&(k-1);
    }
    return count;
    
}
