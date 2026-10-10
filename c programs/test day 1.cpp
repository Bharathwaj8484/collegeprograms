#include<stdio.h>  
int main()    
{    
	int i,fact=1;
	float num;    
	printf("Enter a num: ");    
  	scanf("%f",&num); 
	 int a=(int)num;
	 while(1)
	 {
	 	if (num==0)
	 	{
	 		printf("invalid words");
	 		break;
		}
		if(a="%c")
		{
			printf("in");
			break;
		}
		else
		{
			if (num>=0 && num-a==0)
			{
				for(i=1;i<=a;i++)
					{    
	      				fact=fact*i;    
					}    
	  			printf("Factorial of is: %d",fact);
				break;
			}
			else
			{
				printf("invalid");
				break;
			}
		}
	 }
return 0;  
}  
