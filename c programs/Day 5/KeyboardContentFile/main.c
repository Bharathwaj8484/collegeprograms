#include <stdio.h>
#include <string.h>

int main()  {
    FILE *fp;
    fp = fopen("text.txt", "w+");
    char text[25];

    printf("Enter a text: ");
    scanf("%s", &text);

    fprintf(fp, "%s", text);
    printf("Successful");
}