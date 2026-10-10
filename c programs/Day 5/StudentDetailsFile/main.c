#include <stdio.h>
#include <stdlib.h>

struct studentData
{
    char name[25];
    int rollno;
};


int main()  {
    int i, n;  
    struct studentData s[10];
    FILE *fp;

    printf("Enter no. of students: ");
    scanf("%d", &n);
    
    for (i=0; i<n; i++) {
        printf("Enter name of student %d: ", i+1);
        scanf("%s", &s[i].name);
        printf("Enter rollno of student %d: ", i+1);
        scanf("%d", &s[i].rollno);
    }
    fp = fopen("D:\\Github\\C-Programs-Slot-B\\Day 5\\StudentDetailsFile\\test.txt", "w+");

    for (i=0; i<n; i++) {
        fprintf(fp, "Student %d Name: ", i+1);
        fprintf(fp, "%s \n", s[i].name);
        fprintf(fp, "Student %d Rollno: ", i+1);
        fprintf(fp, "%d \n", s[i].rollno);
    }
    printf("File Created");        
}