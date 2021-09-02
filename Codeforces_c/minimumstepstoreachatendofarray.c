#include<stdio.h>
void main()
{
	int a[100],i,n,c,flag;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	c=0;
	flag=0;
	for(i=0;;)
	{
		if(i<n-1)
		{
			c++;
			i=i+a[i];
		}
		else if(i==n-1)
		{
			if(c==0)
			flag=1;
			break;
		}
		else
		{
		break;
		}
	}
	if(flag==0)
	printf("%d",c);
	else
	printf("-1");
}
