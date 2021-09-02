#include<stdio.h>
void main()
{
	int a[100],i,n,k,b[100],m=0;
	scanf("%d %d",&n,&k);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		if(k>=a[i])
		b[m++]=a[i]+k;
		else
		b[m++]=a[i]-k;
	}
	for(i=0;i<m;i++)
	{
		printf("%d ",b[i]);
	}
	int	min=b[0];
	for(i=1;i<m;i++)
	{
		if(b[i]<min)
		min=b[i];
	}
	int max=b[0];
	for(i=1;i<m;i++)
	{
		if(b[i]>max)
		max=b[i];
	}
	printf("\n%d\n",max-min);
}
