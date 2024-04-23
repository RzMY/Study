#include <iostream>
#include <string>

using namespace std;

class Building;

class LaoWang
{
public:

	LaoWang();
	void visit1();	//让visit1()函数   可以 访问Building中的私有成员
	void visit2();	//让visit2()函数 不可以 访问Building中的私有成员

	Building *building;

private:

	
};

class Building
{
	// 告诉编译器，LaoWang类下的visit1()函数是Building类的好朋友，可以访问Building的私有成员
	friend void LaoWang::visit1();

public:
	Building();

	string m_SittingRoom;	//客厅
private:

	string m_BedRoom;		//卧室
};


LaoWang::LaoWang()
{
	building = new Building;
}

void LaoWang::visit1()
{
	cout << "隔壁老王LaoWang类中的visit1()函数正在访问：" << building->m_SittingRoom << endl;
	cout << "隔壁老王LaoWang类中的visit1()函数正在访问：" << building->m_BedRoom << endl;
}

void LaoWang::visit2()
{
	cout << "隔壁老王LaoWang类中的visit2()函数正在访问：" << building->m_SittingRoom << endl;
	//cout << "隔壁老王LaoWang类中的visit2()函数正在访问：" << building->m_BedRoom << endl;	//错误！私有属性不可访问
}

Building::Building()
{
	m_SittingRoom = "客厅";
	m_BedRoom = "卧室";
}

void test()
{
	LaoWang lw;
	
	lw.visit1();

	lw.visit2();
}

int main()
{
	test();
	
	return 0;
}
