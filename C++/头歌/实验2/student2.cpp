#include <iostream>
using namespace std;

class Student
{
    private:
        int SID;
        string Name;
    public:
        Student();
        Student(int sid, string name);
        ~Student();
};

Student::Student()
{
    SID = 0;
    Name = "王小明";
}

Student::Student(int sid, string name)
{
    SID = sid;
    Name = name;
}

Student::~Student()
{
    cout << SID << " " << Name << " 退出程序" << endl;
}

int main()
{
    int sid1, sid2, sid3;
    string name1, name2, name3;
    cin >> sid1 >> name1;
    cin >> sid2 >> name2;
    cin >> sid3 >> name3;
    Student student1(sid1, name1);
    Student student2(sid2, name2);
    Student student3(sid3, name3);
    Student student0;
    return 0;
}

//测试输入：1 厉宏富 2 冷欣荣 3 鲍俊民