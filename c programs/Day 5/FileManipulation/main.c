#include <stdlib.h>
#include <stdio.h>

int main()  {
    FILE *fp;
    fp = fopen("D:\\Github\\C-Programs-Slot-B\\Day 5\\FileManipulation\\sample.txt", "r+");
    char text[25];

    fscanf(fp, "%s", &text);
    printf("Contents of file: %s \n", text);
    
    fclose(fp);
    printf("File successfully closed!");

}