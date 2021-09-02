#include<stdio.h>
#include<math.h>
int main()
{
	int n,i;
	scanf("%d",&n);
	int ar[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&ar[i]);
	}
	int mi=abs(ar[0]-ar[1]);
	int ma=ar[n-1]-ar[0];
	printf("%d %d\n",mi,ma);
	for(i=1;i<n;i++)
	{
		if(ar[i]<=0)
		{
			int mi=abs(ar[i]-ar[i-1]);
			int ma=ar[n-1]-ar[i];
			printf("%d %d\n",mi,ma);
		}
		else
		{
			int mi=abs(ar[i]-ar[i-1]);
			int ma=ar[i]-ar[0];
			printf("%d %d\n",mi,ma);
		}
	}
}
