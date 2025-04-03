#include <iostream>
using namespace std;

class StInfo
{
    public:
        int SID;
        char *Name;
        char *Class;
        char *Phone;
        void SetInfo(int sid, char *name, char *cla, char *phone);
        void PrintInfo();
};

void StInfo::SetInfo(int sid, char *name, char *cla, char *phone)
{
    SID = sid;
    Name = name;
    Class = cla;
    Phone = phone;
}

void StInfo::PrintInfo()
{
    cout << "学号：" << SID << endl;
    cout << "姓名：" << Name << endl;
    cout << "班级：" << Class << endl;
    cout << "手机号：" << Phone << endl;
}

int main(){
    StInfo jack;
    char name[] = "Jack";
    char cla[] = "计算机202205";
    char phone[] = "18888888888";
    jack.SetInfo(1, name, cla, phone);
    jack.PrintInfo();
    return 0;
}