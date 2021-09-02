#include<stdio.h>
int main()
{
	int n,a,b,d,s=0,c=0;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d %d %d",&a,&b,&d);
		if(a==1)
		c++;
		if(b==1)
		c++;
		if(d==1)
		c++;
		
		if(c>=2)
		s++;
		c=0;
	}
	printf("%d\n",s);
}
