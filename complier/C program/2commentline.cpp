#include<stdio.h>
int main()
{
	char a[100];
	int i,c=0,s=0,v=0;
	printf("\nenter the input line : ");
	scanf("%[^\n]",&a);
	for(i=0;a[i];i++){
		if(a[i]=='/' && a[i+1]=='/' ){
			s=1;
		}
		else if(a[i]=='/' && a[i+1]=='*'){
			v=1;
		}
		c++;
	}
	if(v==1 && a[c-1]=='/' && a[c-2]=='*'){
		printf("this is comment line ");
	}
	else if(s==1 && a[c-1]!='/' && a[c-2]!='*'){
		printf("this is comment line");
	}
	else
	printf("this is not a comment line ");
}

