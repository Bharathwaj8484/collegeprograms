#include <stdio.h>
#include <string.h>

int main()  {
    char username[25], _username[25];

    printf("Enter username: ");
    scanf("%s", &username);
    printf("Re-enter username: ");
    scanf("%s", &_username);

    if(strcmp(username, _username) == 0)    {
        printf("\nUsername is valid");
    } else {
        printf("\nUsername is not valid");
    }
}