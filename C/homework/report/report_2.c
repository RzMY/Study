#include <stdio.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    char gender;
    float gpa;
} Student;

void print_student(Student s) {
    printf("Name: %s\n", s.name);
    printf("Age: %d\n", s.age);
    printf("Gender: %c\n", s.gender);
    printf("GPA: %.2f\n", s.gpa);
}

int main() {
    Student s1;
    strcpy(s1.name, "Qiu");
    s1.age = 20;
    s1.gender = 'M';
    s1.gpa = 4.8;

    print_student(s1);

    return 0;
}
