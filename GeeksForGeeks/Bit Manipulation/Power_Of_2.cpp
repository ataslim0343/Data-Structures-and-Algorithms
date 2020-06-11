/*
Given a positive integer x. The task is to check if x is a power of 2. That is x is 2^i for some i.

*/




#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t-->0)
	{
	    long long int x;
	    cin>>x;
	    if(x==0)
	    {
	      cout<<"NO"<<endl;  
	    }
	    else
	    {
	        if((x & (x-1))==0)
	        {
	            cout<<"YES"<<endl;
	        }
	    else
	        {
	            cout<<"NO"<<endl;
	        }

	    }
	    
	}
	return 0;
}
