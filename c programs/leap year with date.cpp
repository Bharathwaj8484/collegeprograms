#include <stdio.h>
#include <stdlib.h>

int main()  {
float d,m,y;
printf("Enter date: ");
scanf("%f/%f/%f", &d, &m, &y);
while(1)  {
if((d-(int)d==0) && (m-(int)m==0) && (y-(int)y==0) && d<32 && m<13 && d!=0 && m!=0 && y!=0) {
break;
} else {
printf("Invalid date..try again\n");
printf("Enter date: ");
scanf("%f/%f/%f", &d, &m, &y);
}
}

if((int)y%4==0 )  {
printf("\n%d is a leap year", (int)y);
printf("\n%d/%d/%d is the next anniversary",int(d),int(m),int(y+1));
} else  {
printf("\n%d is not a leap year", (int)y);
printf("\n%d/%d/%d is the previous anniversary",int(d),int(m),int(y-1));
}
}
