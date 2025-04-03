#include <iostream>
#include <string>
using namespace std;
 
/********* Begin *********/
// 前置声明 Teacher 类
class Teacher;
 
class Student
{ friend class Teacher;// 声明友元类
  public:
  Student(int num,string nam,string se);
  void Print();
private:
    int number;
    string name;
    string sex;
	
};
//学生类的定义
Student::Student(int num,string nam,string se)
{  
	number=num;
	name=nam;
	sex=se;
}
void Student::Print()
{
	cout<<"学生："<<name<<"，编号："<<number<<"，性别："<<sex<<endl;
}
 
 
 
class Teacher
{public:
    Teacher(int num,string nam,string se);
    void Print();
	Teacher(const Student &s);
	//教师类的声明
 private:
    int number;
    string name;
    string sex;
	
    
    
};
//教师类的定义
Teacher::Teacher(const Student &s)
{  
	number=s.number;
	name=s.name;
	sex=s.sex;
}
void Teacher::Print()
{
	cout<<"教师："<<name<<"，编号："<<number<<"，性别："<<sex<<endl;
}
 
 
/********* End *********/