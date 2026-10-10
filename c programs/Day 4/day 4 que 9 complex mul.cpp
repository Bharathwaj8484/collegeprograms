#include<stdio.h>
#include<conio.h>
struct complex
    {
        int r,i;
    };
        void read(struct complex *);
        
        
        struct complex mul(struct complex *,struct complex *);
        void write(struct complex *);
        int main()
           {
                   struct complex a,b,c,d,e;
                   
                   read(&a);
                   read(&b);
                   
                   e=mul(&a,&b);
                   
                   write(&e);
                   getch();
           }
        void read(struct complex *x)
          {
                 printf("Enter Real Part : ");
                 scanf("%d",&(x->r));
                 printf("Enter Imig Part : ");
                 scanf("%d",&(x->i));
          }
        struct complex mul(struct complex *x,struct complex *y)
         {
                 struct complex z;
                 z.r=(x->r)*(y->r)-(x->i)*(y->i);
                 z.i=(x->r)*(y->i)+(x->i)*(y->r);
                 return(z);
         }
        void write(struct complex *x)
        {
        printf("\nThe no. is= %d+%di",x->r,x->i);
        } 
