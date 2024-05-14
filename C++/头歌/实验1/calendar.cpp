#include <iomanip>
#include <stdio.h>
#include <iostream>
using namespace std;

void printMonth(int year, int month);

int leapYear(int y)
{
    if(y % 4 == 0 && y % 100 != 0 || y % 400 == 0)
        return 1;
    return 0;
}


int whatDay(int year, int month)
{
    if(month==1||month==2)
    {
        month+=12;
        year--;
    }

    int w = (1 + 1 + 2*month + 3*(month+1)/5 + year + year/4 - year/100 + year/400) % 7;
    return w;
}

void printMonth(int year, int month){
    int xq = whatDay(year, month);
    int days = 0;
    if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
        days = 31;
    }else if(month == 4 || month == 6 || month == 9 || month == 11){
        days = 30;
    }else if(month == 2){
        if(leapYear(year)){
            days = 29;
        }else{
            days = 28;
        }
    }
    // cout << "一 二 三 四 五 六 日" << endl;
    // for(int i = 1; i < xq; i++){
    //     cout << "   ";
    // }
    // for(int i = 1; i <= days; i++){
    //     if((i + xq - 2) % 7 == 0){
    //         cout << endl;
    //     }
    //     if(i < 10){
    //         cout << " ";
    //     }
    //     cout << i << " ";
    // }
    // cout << endl;
    cout << "  一  二  三  四  五  六  日" << endl;
    for(int i = 1; i < xq; i++){
        cout << setw(4) << " ";
    }
    for(int i = 1; i <= days; i++){
        if((i + xq - 2) % 7 == 0){
            cout << endl;
        }
        cout << setw(4) << right << i;
    }
    cout << endl;
}

int main()
{
  
    int y, m;

    cin >> y >> m;

    printMonth(y,m);

    return 0;
}