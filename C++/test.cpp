#include <iostream>

class Date
{
    private:
        int day, month, year;
    public:
        Date(int year, int month, int day){
            this->year = year;
            this->month = month;
            this->day = day;
        }
        // Date(int year, int month, int day):year(year), month(month), day(day) {
        //     std::cout << "Date(int year, int month, int day)" << std::endl;
        // }
        int getYear() { return year; }
        void setDate(int y, int m, int d);
        bool isLeapYear(int year);
        void printDate();
};
void Date::setDate(int y, int m, int d)
{
    year = y;
    month = m;
    day = d;
}
bool Date::isLeapYear(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}
void Date::printDate()
{
    std::cout << year << "年" << month << "月" << day << "日" << std::endl;
}


int main()
{
    Date today(2024, 3, 14);
    std::cout << "该年" << today.getYear() << (today.isLeapYear(2024) ? "是" : "不是") << "闰年" << std::endl;
    int year, month, day;
    std::cout << "请输入年月日：";
    std::cin >> year >> month >> day;
    today.setDate(year, month, day);
    std::cout << "该年" << today.getYear() << (today.isLeapYear(2024) ? "是" : "不是") << "闰年" << std::endl;
    today.printDate();
}
```