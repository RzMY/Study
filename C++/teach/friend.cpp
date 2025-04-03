#include <iostream>
#include <string>

using namespace std;

// 房屋类
class Building
{
	// 告诉编译器 laoWang全局函数是 Building类  的好朋友，可以访问Building对象的私有成员
	friend void laoWang1(Building *building);
	friend void laoWang2(Building &building);
	friend void laoWang3(Building building);

public:

	Building()
	{
		m_SittingRoom = "客厅";
		m_BedRoom = "卧室";
	}
	
	string m_SittingRoom;	// 客厅

private:

	string m_BedRoom;		// 卧室
};



//全局函数
void laoWang1(Building *building)
{
	cout << "隔壁老王 全局函数 正在访问：（地址传递） " << building->m_SittingRoom << endl;

	cout << "隔壁老王 全局函数 正在访问：（地址传递） " << building->m_BedRoom << endl;
}

void laoWang2(Building &building)
{
	cout << "隔壁老王 全局函数 正在访问：（引用传递） " << building.m_SittingRoom << endl;

	cout << "隔壁老王 全局函数 正在访问：（引用传递） " << building.m_BedRoom << endl;
}

void laoWang3(Building building)
{
	cout << "隔壁老王 全局函数 正在访问：（ 值传递 ） " << building.m_SittingRoom << endl;

	cout << "隔壁老王 全局函数 正在访问：（ 值传递 ） " << building.m_BedRoom << endl;
}

void test()
{
	Building building;
	laoWang1(&building);
	laoWang2(building);
	laoWang3(building);
}


int main()
{
	test();
}