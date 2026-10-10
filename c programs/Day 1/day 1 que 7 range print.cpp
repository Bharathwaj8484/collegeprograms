#include<stdio.h>
int main() {
 int num,m,n;
 
 printf ("Enter range (m, n ) : ") ;
 scanf ("%d %d", &m, &n);
 for (num = m; num <= n; num++) {
   printf("%d ", num);
 }
 
}
