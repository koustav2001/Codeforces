#include<stdio.h>
int main()
{
	long n;
	scanf("%lld",&n);
	if(n%2==0)
	{
		if(n%4!=0)
		printf("%d",n/4);
		else
		printf("%d",n/4-1);
	}
	else
	printf("0");
}
