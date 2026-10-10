#include <stdio.h>
#include <stdlib.h>

int main()  {
    FILE *fp;
    fp = fopen("D:\\Github\\C-Programs-Slot-B\\Day 5\\HandleFileError\\sampl.txt", "r");
    if(fp == NULL)   {
        puts("Error! File not found! Exiting....");
        exit(-1);
    } else {
        printf("File is present at location!");
    }
}