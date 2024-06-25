#include<fstream> 
#include<string>
#include<iomanip>
#include<iostream>
#include<cstring>
using namespace std;

class CStudent //定义学生类
{
    char name[20];
    int number;
    double english;
    double math;
    public:
    CStudent(const char* str="",int num=0,double en=0,double ma=0);   //构造函数
    void display();             //显示数据成员
    void datatofile(ofstream &out);   //把数据写入文件 
    void datafromfile(ifstream &in);  //从文件读出数据
};

CStudent::CStudent(const char *str,int num,double en,double ma)
{
    strcpy(name,str);
    number=num;
    english=en;
    math=ma;
}

void CStudent::display()
{
    cout.setf(ios::left);
    cout<<setw(20)<<name;
    cout.unsetf(ios::left); 
    cout.setf(ios::right);   
    cout<<setw(10)<<number<<setw(10)<<english<<setw(10)<<math<<endl;
}

void CStudent::datatofile(ofstream &out)
{
    out.write(name,20);
    out.write((char*)&number,sizeof(int));
    out.write((char*)&english,sizeof(double));
    out.write((char*)&math,sizeof(double));
}

void CStudent::datafromfile(ifstream &in) 
{
    in.read(name,20);
    in.read((char*)&number,sizeof(int));
    in.read((char*)&english,sizeof(double));
    in.read((char*)&math,sizeof(double));
}

int main() {

    char name[20];
    int number;
    double english, math;

    std::cout << "请输入学生姓名：";
    std::cin >> name;
    std::cout << "请输入学生学号：";
    std::cin >> number;
    std::cout << "请输入英语成绩：";
    std::cin >> english;
    std::cout << "请输入数学成绩：";
    std::cin >> math;

    CStudent stu1(name, number, english, math);
    std::ofstream dtof("s.dat", std::ios::out | std::ios::binary);
    stu1.datatofile(dtof);

    std::cout << "学生1:" << std::endl;
    stu1.display();
    dtof.close();

    std::cout << std::endl;

    CStudent s1;
    int i=0;
    std::ifstream dfromf("s.dat", std::ios::in | std::ios::binary);
    while(1)
    {
        s1.datafromfile(dfromf); 
        i++;
        if(dfromf.eof()!=0)break;
        std::cout << "第" << i << "个学生：" << std::endl;
        s1.display();
        std::cout << "读文件成功" << std::endl; 
    }

    std::cout << "test" << std::endl;

    CStudent stu2("李四",200508298,83,76.5);
    CStudent stu3("王五",200508299,45,70.5);
    CStudent stu4("二马", 200533456, 85, 60);

    dtof.open("s.dat", std::ios::app | std::ios::binary);
    stu2.datatofile(dtof);
    stu3.datatofile(dtof);
    stu4.datatofile(dtof);
    dtof.close();

    // 替换第二个学生
    dtof.open("s.dat", std::ios::in | std::ios::out | std::ios::binary);
    dtof.seekp(sizeof(CStudent), std::ios::beg);
    stu4.datatofile(dtof);
    dtof.close();

    dfromf.clear();
    dfromf.seekg(0, std::ios::beg);

    i=0;
    while(1)
    {
        s1.datafromfile(dfromf); 
        i++;
        if(dfromf.eof()!=0)break;
        std::cout << "第" << i << "个学生：" << std::endl;
        s1.display();
        std::cout << "读文件成功" << std::endl; 
    }

    dfromf.close();
    return 0;
}