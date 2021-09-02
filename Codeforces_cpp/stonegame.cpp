#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int i;
		int pos1=0;
		int pos2=0;
		int a[n];
		for(i=0;i<n;i++)
		cin>>a[i];
		for(i=0;i<n;i++)
		{
			if(a[i]<a[pos1])
			{
				pos1=i;
			}
			if(a[i]>a[pos2])
			{
				pos2=i;
			}
			
		}
	}
}
