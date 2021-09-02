#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long n;
        cin>>n;
        long long c2=0,c3=0;
        while(!(n%2))
        {
            n/=2;
            c2++;
        }
        while(!(n%3))
        {
            n/=3;
            c3++;
        }
        if(n!=1 || c2>c3)
        cout<<-1<<endl;
        else
        cout<<(c3-c2)+c3<<endl;
    }
}