#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	string str;
	cin>>str;
	int n = str.size();
    bool dp[n][n];
    memset(dp, 0, sizeof(dp));
    for(int i = 0; i < n; i++){
        dp[i][i] = true;
    }
    int start = 0;
    int maxlength = 1;
    for(int i = 0; i < n - 1; i++){
        if(str[i] == str[i + 1]){
            dp[i][i + 1] = true;
            start = i;
            if(maxlength == 1){
                start = i;
                maxlength = 2;
            }
            else{
                start = min(i, start);
                maxlength = 2;
            }
        }
        //else dp[i][i + 1] = 0;
    }
    for(int k = 3; k <= n; k++){
        for(int i = 0; i < n - k + 1; i++){
            int j = i + k - 1;
            if(dp[i + 1][j - 1] && str[i] == str[j]){
                dp[i][j] = true;
                if(k > maxlength){
                    maxlength = k;
                    start = i;
                }
            }
                else if(k == maxlength){
                    start = min(i , start);
                }
            }
        }
	//cout<<start;
	cout<<str.substr(start,maxlength);
}

