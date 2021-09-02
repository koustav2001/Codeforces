#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
    long n,i,s=0,even=0,odd=0;
    cin>>n;
    long ar[n];
    for(i=0;i<n;i++)
    {
        cin>>ar[i];
        if(ar[i]%2!=0)
        odd+=1;
        else
        even+=1;
        s=s+ar[i];
    }
    //cout<<s<<endl;
    if(s%2!=0||(even>0 && odd>0))
    cout<<"YES\n";
    else
    cout<<"NO\n";
    }
}