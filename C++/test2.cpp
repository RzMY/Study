#include<iostream>
#include<string>
using namespace std;
class Student {
private:
	string stu_id;
	string name;
	float score;
	static float all_score;
	static int num;
	static float ave;
public:
	Student(string s, string n, float sco);
	void disp1();
	void disp2();

};

int Student::num = 0;
float Student::all_score = 0.0;
float Student::ave = 0.0;

Student::Student(string s, string n, float sco)
{
	stu_id = s;
	name = n;
	score = sco;
	++num;
	all_score =all_score + score;
	ave = all_score / num;
}
void Student::disp1()
{
	cout << "姓名:" << name << endl;
	cout << "学号:" << stu_id << endl;
	cout << "成绩:" << score << endl << "--------------------------------------" << endl;

}
void Student::disp2()
{
	cout << "学生人数:" << num << endl;
	cout << "平均成绩:" << ave << endl;
}
int main()
{
	Student stu[10] = {
		Student("202205123", "刘一", 91.5),
		Student("202205124", "陈二",96.5),
		Student("202205125", "张三", 85.6),
		Student("202205126", "李四", 53.8),
		Student("202205127", "王五", 86.4),
		Student("202205128", "赵六",53.4),
		Student("202205129", "孙七",69.7),
		Student("202205130", "周八",83.5),
		Student("202205131", "吴九", 89.6),
		Student("202205132", "郑十", 99.1)
	};
	for (int i = 0; i < 10; i++)
	{
		stu[i].disp1();
	}
	stu[0].disp2();

}