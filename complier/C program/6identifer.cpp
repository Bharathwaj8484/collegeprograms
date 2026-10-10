#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_IDENT_LEN 100

int isValidIdentifier(char *ident) {
  int i, len = strlen(ident);
  if (!isalpha(ident[0]) && ident[0] != '_') {
    return 0;
  }
  for (i = 1; i < len; i++) {
    if (!isalnum(ident[i]) && ident[i] != '_') {
      return 0;
    }
  }
  return 1;
}

int main() {
  char ident[MAX_IDENT_LEN];
  printf("Enter an identifier: ");
  scanf("%s", ident);
  if (isValidIdentifier(ident)) {
    printf("Valid identifier\n");
  } else {
    printf("Invalid identifier\n");
  }
  return 0;
}


