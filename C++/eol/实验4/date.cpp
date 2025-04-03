#include "date.h"

Date::Date(int year, int month, int day):year(year), month(month), day(day), totalDays(0){
    int months[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    for(int y = 1; y < year; y++){
        totalDays += (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0) ? 366 : 365;
    }
    for(int m = 1; m < month; m++){
        totalDays += months[m];
    }
    totalDays += day;
    if(isLeapYear() && month > 2){
        totalDays++;
    }
}

void Date::show() const{
    cout << year << "-" << month << "-" << day << endl;
}

bool Date::isLeapYear() const{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int Date::distance(const Date& date) const{
    return totalDays - date.totalDays;
}

std::ostream& operator<<(std::ostream& os, const Date& date){
    os << date.year << "-"
       << std::setw(2) << std::setfill('0') << date.month << "-"
       << std::setw(2) << std::setfill('0') << date.day;
    return os;
}