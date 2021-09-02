#include<stdio.h>
int main()
{
	int m,n,max;
	scanf("%d %d",&m,&n);
	max=(m*n)/2;
	if((m*n)%2==0 || (m*n)%2==1 )
	printf("%d",max);
}
