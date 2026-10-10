#include <stdio.h>

int main()  {
    FILE *fp;
    char text[10]="Hello", file[10]= "hi.txt";
    fp = fopen(file, "w+");
    fprintf(fp, "%s", text);
    printf("File Content: %s", text);
}