#include<stdio.h>
int main() 
{
	 int num,m,n,r,a,p=1;
	 printf ("Enter range (m, n ) : ") ;
	 scanf ("%d %d", &m, &n);
	 a=n-m;
	 while(1)
 		{
 			if (m<=0 || n<=0 )
 		{
 			printf("enter pos num");
 			break;
		}
		printf("enter postion to leave ");
 		scanf("%d",&r);
 		if (n<=m)
 		{
 			printf("enter good range");
 			break;
		 }
		 if (a<r || a<=0)
 		{
 			printf("out of range");
 			break;
		 }
	 for (num = m; num <= n; num++)
	 	{
	   		if (p==r)
	   		{
			  	p++;
				continue;
			}
			else 
			{
				printf("%d ", num);
			  	p++;
			}
	 	}
	break;
 	
 }
 
 }
