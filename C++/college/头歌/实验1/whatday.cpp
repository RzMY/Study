#include <iostream>
using namespace std;


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

int main()
{

    int y, m, xq;
    cin >> y >> m;

    xq = whatDay(y,m);

    cout << y << "年" << m << "月1日是星期";
    if(xq == 7)
        cout << "日" << endl;
    else
        cout << xq << endl;
    return 0;
}