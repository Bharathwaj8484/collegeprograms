#include<stdio.h>
int main()
{
	int a,b=1;
	while (b==1)
	{
	printf(" enter no of kms: ");
	scanf("%d",&a);
	printf(" the total kms %d",a*10);
	printf("\n1.Continue\n2.Exit\nEnter your choice ");
	scanf("%d",&b);
	}
}
