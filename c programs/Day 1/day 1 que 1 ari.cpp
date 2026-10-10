#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
int c,a,b;
printf("enter two integer");
scanf("%d %d",&a,&b);
while(1)
{
printf("\n1.add \t2.multi\t 3.sub\n");
printf("4.div\t 5.mod\t 6.exit\n");
printf("enter choice: ");
scanf("%d",&c);
switch(c)
{
case 1:
printf("add: %d",a+b);
break;
case 2:
printf("multi: %d",a*b);
break;
case 3:
printf("sub: %d",a-b);
break;
case 4:
printf("div: %d",a/b);
break;
case 5:
printf("mod: %d",a%b);
break;
default:
	exit(0);
break;
}
}
return 0;
}
