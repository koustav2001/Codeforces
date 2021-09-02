#include<stdio.h>
#include<string.h>
void main()
{
	int n,result;
	char a[100];
	scanf("%d",&n);
	while(n--)
	{
		scanf("%s",a);
		if(strlen(a)<10)
		{
			printf("%s\n",a);
		}
		else
		{
		printf("%c%d%c\n",a[0],strlen(a)-2,a[strlen(a)-1]);
		}
	}
}
