#include <stdio.h>
#include <stdlib.h>

int main()
{
    int rows,i,j,space,count=1;
    printf("Number of rows:");
    scanf("%d",&rows);
    for(i=0; i<=rows; i++){
        for(space=1; space<=rows-i; space++ ){
            printf(" "); 
        }
        for(j=0; j<=i; j++)
        {
            if(j==0 || i==0)
                count=1;
            else
                count=count*(i-j+1)/j;
            printf("%4d ",count);
        }
        printf("\n");
    }
    return 0;
}