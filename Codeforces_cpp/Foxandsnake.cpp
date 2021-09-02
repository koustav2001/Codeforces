#include<iostream>
using namespace std;
int main()
{
    int i,n,m,j;
    cin>>n>>m;
    for(i=1;i<=n;i++)
    {
        int f=0;
        if(i%4==2)
        {
            for(j=1;j<m;j++)
            cout<<".";
            cout<<"#";
        }
        else if(i%4==0)
        {
            cout<<"#";
            for(j=2;j<=m;j++)
            {
                cout<<".";
            }
        }
        else if(i%2!=0)
        {
            for(j=1;j<=m;j++)
            cout<<"#";
        }
        cout<<endl;
    }
}
