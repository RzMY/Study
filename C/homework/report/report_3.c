#include <stdio.h>
#include <string.h>

/*
 * 文件名称：student_info.c
 * 版权说明：版权所有(C) 2024
 * 版本号：1.0
 * 更改日期：2024-06-29
 * 作者：QiuZS
 * 内容：实现学生信息的结构体定义和基本操作
 * 功能：定义学生信息的结构体，提供打印学生信息的函数
 * 修改日志：
 *    - 2024-06-29：初始版本
 */

// 学生信息结构体
typedef struct {
    char name[50];   // 学生姓名
    int age;         // 学生年龄
    char gender;     // 学生性别，'M' 表示男，'F' 表示女
    float gpa;       // 学生的GPA
} Student;

/*
 * 函数名称：print_student
 * 功能：打印学生的信息
 * 参数：
 *   - s：Student结构体类型，包含学生的所有信息
 * 返回值：无
 */
void print_student(Student s) {
    printf("Name: %s\n", s.name);  // 输出学生姓名
    printf("Age: %d\n", s.age);    // 输出学生年龄
    printf("Gender: %c\n", s.gender);  // 输出学生性别
    printf("GPA: %.2f\n", s.gpa);  // 输出学生GPA
}

/*
 * 函数名称：main
 * 功能：程序的入口点，创建学生对象并打印其信息
 * 参数：无
 * 返回值：int类型，返回0表示程序成功执行
 */
int main() {
    Student s1;  // 声明一个Student结构体类型的变量s1

    // 初始化学生s1的信息
    strcpy(s1.name, "Qiu");  // 设置姓名为Qiu
    s1.age = 20;               // 设置年龄为20
    s1.gender = 'M';           // 设置性别为男
    s1.gpa = 4.8;              // 设置GPA为4.8

    // 调用函数打印学生s1的信息
    print_student(s1);

    return 0;  // 返回0，表示程序成功执行
}