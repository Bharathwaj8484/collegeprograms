#include<stdio.h>
int main() 
{
	int t,stu,stf,a,b;
	printf("Enter total user ");
	scanf("%d",&t);
		printf("Enter stf user ");
		scanf("%d",&stf);
	while(1)
	{
		if (t<=stf || t<0 || stf<0)
		{
			printf("enter valid input");
			break;
		}
		else
		{
			a=stf/3;
			stu=t-(stf+a);
			if (stu<=0)
			{
				printf("there are no students");
				break;
			}
			else
			{
				printf("\nNumber of student ");
				printf("%d",stu);
			}
			printf("\n%d number of Non teaching staff",a);
			break;
		}
	}
}
