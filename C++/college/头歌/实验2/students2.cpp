#include <string>
#include <iostream>
using namespace std;
 
class Student
{
    //成员声明
public:
    int SID;
    string Name;
    float Sco;
    Student();
    Student(int sid,string name,float sco)
    {
        SID = sid;
        Name = name;
        Sco = sco;
    }
};
Student stu[5];
int num = 0;
 
Student::Student()//构造函数
{}
 
void Add(int sid, string name, float sco)
{
    
    stu[num] = Student(sid, name, sco);
    num++;
    
}
 
void PrintAll()
{
    
    //打印表格内容
    for (int j = 0; j < num; j++)
    {
        cout << stu[j].SID << " " << stu[j].Name << " " << stu[j].Sco << endl;
    }
    
}
 
void Average()
{
    
    //计算并打印出平均成绩
    float sum = 0.00;
    float ave;
    for (int j = 0; j < num; j++)
    {
        sum += stu[j].Sco;
    }
    ave = sum / num;
    cout << "平均成绩" << " " << ave << endl;
}
    
int main()
{
    int i, j, k;
    string name1, name2, name3;
    float score1, score2, score3;
    cin >> i >> name1 >> score1;
    cin >> j >> name2 >> score2;
    cin >> k >> name3 >> score3;
    Add(i, name1, score1);
    Add(j, name2, score2);
    Add(k, name3, score3);
    PrintAll();
    Average();
}