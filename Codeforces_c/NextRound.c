#include<stdio.h>
int main()
{
	int n,k,i,a[100];
	scanf("%d %d",&n,&k);
	int count=0;
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		if(a[i]>0 && a[i]>=a[k-1])
		count++;
	}
	printf("%d",count);
}
