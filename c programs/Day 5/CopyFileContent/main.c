#include <stdio.h>
#include <stdlib.h>

int main()  {
    FILE *fp1, *fp2;
    char text[25];
    fp1 = fopen("D:\\Github\\C-Programs-Slot-B\\Day 5\\CopyFileContent\\a.txt", "r");
    fp2 = fopen("D:\\Github\\C-Programs-Slot-B\\Day 5\\CopyFileContent\\b.txt", "w");
    
    fscanf(fp1, "%s", &text);
    fprintf(fp2, "%s \n", text);

    printf("Contenst of file 1 sucessfullt copied to file 2");
}