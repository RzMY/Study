#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct Node
{
    char name[10];
    int id;
}Name_list;


int id_list[1050000];// 存放每个id对应的name_list的下标
Name_list name_list[100];// 存放每个人的名字
int people_num;
int sentence_num;

/*
John
  Robert
    Frank
    Andrew
  Nancy
    David
*/

// 创建家谱
void createGenealogy(){

    scanf("%d %d", &people_num, &sentence_num);
    int count = 0;
    char name[10];
    int id = 1;
    int space_num = 0;
    int space[200];// 存放每个空格数对应的id

    memset(id_list, -1, sizeof(id_list));
    memset(space, -1, sizeof(space));

    // 读写第一个人名
    scanf("%s", name);
    strcpy(name_list[count].name, name);
    name_list[count].id = id;
    id_list[id] = count++;
    space[space_num] = id;
    
    while(count != people_num){
        getchar();// 跳过\n
        char s;
        space_num = 0;
        while(1){
            s = getchar();
            if(s == ' '){
                s = getchar();
                space_num += 2;// 遇到空格
            }else{
                ungetc(s, stdin);
                break;// 遇到人名
            }
        }
        if(space[space_num] == -1){ // 检查是否有同缩进的
            id = space[space_num - 2] * 2;// 没有同缩进的，id为父节点的两倍
        }else{
            id = space[space_num] + 1;// 有同缩进的，id为兄弟节点的加一
        }

        // 读写人名
        scanf("%s", name);
        strcpy(name_list[count].name, name);
        name_list[count].id = id;
        id_list[id] = count++;
        space[space_num] = id;
    }
}

/*
X is a child of Y
X is the parent of Y
X is a sibling of Y
X is a descendant of Y
X is an ancestor of Y
*/

// 根据名字找到id
int findId(char name[]){
    for(int i = 0; i <= people_num; i++){
        if(strcmp(name_list[i].name, name) == 0){
            return name_list[i].id;
        }
    }
    return -1;
}

// 根据id找到名字
char* findName(int id){
    return name_list[id_list[id]].name;
}

// 是否是子女
bool isChild(char person_a[], char person_b[]){
    int id_a = findId(person_a);
    return strcmp(findName(id_a / 2), person_b) == 0;
}

// 是否是父母
bool isParent(char person_b[], char person_a[]){
    int id_a = findId(person_a);
    return strcmp(findName(id_a / 2), person_b) == 0;
}

// 是否是兄弟
bool isSibling(char person_a[], char person_b[]){
    int id_a = findId(person_a);
    int id_b = findId(person_b);
    return id_a / 2 == id_b / 2;
}

// 是否是后代
bool isDescendant(char person_a[], char person_b[]){
    int id_a = findId(person_a);
    int id_b = findId(person_b);
    while(id_a != 0){
        id_a /= 2;
        if(id_a == id_b){
            return true;
        }
    }
    return false;
}

// 是否是祖先
bool isAncestor(char person_b[], char person_a[]){
    int id_a = findId(person_a);
    int id_b = findId(person_b);
    while(id_a != 0){
        id_a /= 2;
        if(id_a == id_b){
            return true;
        }
    }
    return false;
}

// 分类检查句子
bool checkSentence(char str[6][10]){

    char person_a[10];
    char person_b[10];
    char relation[10];

    strcpy(person_a, str[0]);
    strcpy(person_b, str[5]);
    strcpy(relation, str[3]);

    switch (relation[0])
    {
    case 'c':
        return isChild(person_a, person_b);
    case 'p':
        return isParent(person_a, person_b);
    case 's':
        return isSibling(person_a, person_b);
    case 'd':
        return isDescendant(person_a, person_b);
    case 'a':
        return isAncestor(person_a, person_b);
    }
}

int main(){
    createGenealogy();

    // 测试

    // for(int i = 0; i <= people_num; i++){
    //     printf("%d %s\n", i, name_list[i]);
    // }
    // for(int i = 0; i <= people_num; i++){
    //     printf("%d %d\n", i, id_list[i]);
    // }
    // char str1[6][10];
    // scanf("%s %s %s %s %s %s", str1[0], str1[1], str1[2], str1[3], str1[4], str1[5]);
    // printf("%s\n", checkSentence(str1) ? "True" : "False");
    
    char str[6][10];// 存放每个句子的单词
    bool result[sentence_num];// 存放每个句子的结果
    int count = sentence_num;
    // 循环检查每个句子
    while(count--){
        scanf("%s %s %s %s %s %s", str[0], str[1], str[2], str[3], str[4], str[5]);
        result[count] = checkSentence(str);
    }
    // 输出结果
    for(int i = sentence_num - 1; i >= 0; i--){
        printf("%s\n", result[i] ? "True" : "False");
    }
    return 0;
}