#include <stdio.h>
int main()
{
   float year;
   printf("Enter a year: ");
   scanf("%f", &year);
   int a=int(year);
   while (1)
   {
   	if (a==0)
	   {
	   		printf("invalid words");
	   }
	else
		{
			if (a%4 ==0 && year-a==0)
				{
			    	printf("%d is a leap year.",a);
				}
			else 
				{
				    printf("%f is not a leap year.", year);
				}
		}

   return 0;
}
}
