#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int sumDigit();

int main()  {
    int n, m, size, result;

    printf("Enter the no.of digits: ");
    scanf("%d", &m);
    if(m == 0)  {
        printf("Error! no.of digits cannot be zero");
        exit(-1);
    }

    printf("Enter a number: ");
    scanf("%d", &n);

    size = log10(n)+1;

    if(size == m)   {}
    else {
        printf("Size not equal!");
        exit(-1);
    }
    
    result = sumDigit(n);
    printf("Sum of Digit: %d", result);
}

int sumDigit(int a)  {
    int k, sum=0;
    while(a != 0)   {
        k = a%10;
        sum += k;
        a /= 10;
    }
    return sum;
}
