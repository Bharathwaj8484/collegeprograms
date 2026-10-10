#include<stdio.h>
#include<conio.h>
struct complex
    {
        int r,i;
    };
        void read(struct complex *);
        struct complex sub(struct complex *,struct complex *);
        void write(struct complex *);
        int main()
           {
                   struct complex a,b,c,d,e;
                   read(&a);
                   read(&b);
                   
                   d=sub(&a,&b);
                   
                   
                   write(&d);
                   
                   getch();
           }
        void read(struct complex *x)
          {
                 printf("Enter Real Part : ");
                 scanf("%d",&(x->r));
                 printf("Enter Imig Part : ");
                 scanf("%d",&(x->i));
          }
        
        struct complex sub(struct complex *x,struct complex *y)
          {
                struct complex z;
                z.r=x->r-y->r;
                z.i=x->i-y->i;
                return(z);
          }
        
        void write(struct complex *x)
        {
        printf("\nThe sub value is= %d+%di",x->r,x->i);
        }
