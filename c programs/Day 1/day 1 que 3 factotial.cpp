#include<stdio.h>
int main()    
{
	int i,f=1,n;    
	printf("Enter a number: ");    
	scanf("%d",&n);    
    if (n>0)
	{
		for(i=1;i<=n;i++)
		{    
      		f=f*i;    
		} 
	printf("Factorial of %d is: %d",n,f);    
	}
	else
		{
			printf("enter postive interger");
		}   
	return 0;  
} 
