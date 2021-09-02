#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long w,h,n,c=1;
        cin>>w>>h>>n;
        while(w%2==0)
        {
            w=w/2;
            c=2*c;
        }
        while(h%2==0)
        {
            h=h/2;
            c=2*c;
        }
        if(h%2!=0 && w%2!=0 && n==1)
        cout<<"YES\n";
        else if(c>=n)
        cout<<"YES\n";
        else
        cout<<"NO\n";
    }
}