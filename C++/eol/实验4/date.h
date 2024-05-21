#ifndef DATE_H
#define DATE_H
#include <ostream>
#include <iomanip>
#include <iostream>
using namespace std;

class Date
{
    int year, month, day;
    int totalDays;   //该日期是从公元元年1月1日开始的第几天
    public:
        Date(int year, int month, int day);	
        int getYear() const { return year; }
        int getMonth() const { return month; }
        int getDay() const { return day; }
        void show() const;			//输出当前日期
        bool isLeapYear() const;	//判断当年是否为闰年
        int distance(const Date& date) const;//计算当前日期与指定日期之间相差天数
        int operator-(const Date& date) const { return distance(date); } // -运算符重载
        friend ostream& operator<<(ostream& os, const Date& date); // <<运算符重载
};

#endif