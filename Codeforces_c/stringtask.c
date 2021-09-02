#include<stdio.h>
int main()
{
	char s[100];
	int i;
	scanf("%s",s);
	strlwr(s);
	for(i=0;i<strlen(s);i++)
	{
		if(s[i]!='a' && s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u' && s[i]!='y')
		{
			printf(".%c",s[i]);
		}
		else
		continue;
	}
}
