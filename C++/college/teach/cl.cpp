#include <iostream>
#include <string>

using namespace std;

// 类作友元

class Building;
class LaoWang
{
public:

	LaoWang();

	void visit();	//参观函数  访问Building中的属性

	Building * building;


private:


};

// 房屋类
class Building
{
	// 告诉编译器，LaoWang类是Building类的好朋友，可以访问Building类的私有成员
	friend class LaoWang;
public:
	
	Building();
		
	string m_SittingRoom;	// 客厅
	
private:
	
	string m_BedRoom;		// 卧室
};

// 类外定义成员函数

Building::Building()
{
	m_SittingRoom = "客厅";
	m_BedRoom = "卧室";
}

LaoWang::LaoWang()
{
	// 创建建筑物对象
	building = new Building;
}

void LaoWang::visit()
{
	cout << "隔壁老王LaoWang类正在访问：" << building->m_SittingRoom << endl;

	cout << "隔壁老王LaoWang类正在访问：" << building->m_BedRoom << endl;
}

void test()
{
	LaoWang lw;
	lw.visit();
}

int main()
{
	char str[] = "Hello, World!";
	cout << str << endl;
	test();

	return 0;
}
