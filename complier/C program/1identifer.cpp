#include<stdio.h>
#include<string.h>
int main()
{
	char string[30];
	printf("Enter the string:");
	scanf("%s",&string);
	if(string[0] >=97 && string[0] <=122)
	
 {
 	printf("The string is valid identifier");  
 }
 else
 {
 	printf("The string is not a valid identifier");
 }
 return 0;
}
