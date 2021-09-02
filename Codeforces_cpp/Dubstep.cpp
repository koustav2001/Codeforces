#include<iostream>
using namespace std;
int main()
{
    int i;
    string s;
    cin>>s;
    for(i=0;i<s.size();)
    {
        if(s[i]=='W' && s[i+1]=='U' && s[i+2]=='B')
        {
        i=i+3;
        cout<<" ";
        }
        else
        {
        cout<<s[i];
        i=i+1;
        }
    }
}