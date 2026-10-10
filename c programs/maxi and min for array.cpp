#include <stdio.h>
#include <stdlib.h>

int main()  {
    int i, j, m, n, s, temp, min, max, sum, diff, arr[] = {17, 16, 18, 13, 11, 15};
    s = sizeof(arr) / sizeof(arr[1]);

    printf("Enter the value of M: ");
    scanf("%d", &m);
    while(m<=0){
        printf("Invalid value....try again!\n");
        printf("Enter the value of M: ");
        scanf("%d", &m);
    }

    printf("Enter the value of N: ");
    scanf("%d", &n);
    while(n<=0) {
        printf("Invalid value....try again!\n");
        printf("Enter the value of N: ");
        scanf("%d", &n);
    }


    for (i=0; i<s; i++) {
        for (j=i + 1; j<s; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    min = arr[n-1];

    for (i=0; i<s; i++) {
        for (j=i + 1; j<s; j++) {
            if (arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    max = arr[m-1];

    sum = max+min;
    diff = max-min;

    printf("Max: %d\nMin: %d\n", max, min);
    printf("Sum: %d\nDiff: %d\n", sum, diff);

}
