#include <stdio.h> 
 
int main()
{ 
 char r;
 float principle, rate, sinterest;
 int time;
 printf("enter senior(y/n)");
 scanf("%c",&r);
 printf("Enter Principle and Time\n");
 scanf ("%f %d",&principle,&time);
	switch(r)
	{
	case 'y':
			rate=12.0;
			sinterest = (principle * rate * time)/ 100.0;	
			break;	
	case 'n':
			rate=10.0;
 			sinterest = (principle * rate * time)/ 100.0;
 			break;
 	default:
 		printf("error");
 		
	 }
 printf ("Principle Amount = %5.2f\n", principle);
 printf ("Rate %% per Annum   = %5.2f%\n", rate);
 printf ("Time   = %d years\n", time);
 printf ("Simple Interest  = %5.2f\n", sinterest);
}
