#include <stdio.h>

int main()  {
    FILE *fp;
    char text[10];
    fp = fopen("D:\\Github\\C-Programs-Slot-B\\Day 5\\ScanFile\\sample.txt", "r");
    fscanf(fp, "%s", &text);
    printf("File Content: %s", text);
}