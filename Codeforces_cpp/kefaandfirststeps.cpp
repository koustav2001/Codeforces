#include<iostream>
using namespace std;
int main()
{
    int n,i,m=0;
    cin>>n;
    long ar[n];
    for(i=0;i<n;i++)    //2 2 9
    {
        cin>>ar[i];
    }
    int left=0,right=0;
    for(i=1;i<n;i++)
    {
        if(ar[left]<=ar[i])
        {
        right=i;
        //cout<<right<<endl;
        }
        else
        {
        m=max(m,right-left+1);
        //cout<<m<<endl;
        left=right+1;
        }
    }
    cout<<m;
}