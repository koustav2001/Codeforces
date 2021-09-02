#include<stdio.h>
int main()
{
	int n,cnt;
	scanf("%d",&n);
	char a[100];
	cnt=0;
	while(n--)
	{
		scanf("%s",a);
		if(a[1]=='+')
		cnt++;
		else
		cnt--;
	}
	printf("%d",cnt);
}
