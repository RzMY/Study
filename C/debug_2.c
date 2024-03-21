#include <stdio.h>
#include <string.h>

struct Person
{
    char name[10];
    int height;
    int age;
};

typedef struct Person Person;

int main()
{
    struct Person ZhangMenJie;

    ZhangMenJie.height = 180;
    ZhangMenJie.age = 20;
    strcpy(ZhangMenJie.name, "ZhangMenJie");
    printf("%s %d %d\n", ZhangMenJie.name, ZhangMenJie.height, ZhangMenJie.age);

    // struct Person QiuZonSen;
    Person QiuZonSen;
    strcpy(QiuZonSen.name, "QiuZonSen");
    printf("%s",QiuZonSen.name);
    return 0;
}