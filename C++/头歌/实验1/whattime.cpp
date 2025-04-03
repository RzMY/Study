#include <iostream>
using namespace std;

void whatTime(int secs, int &h, int &m, int &s)
{
    h = secs / 3600;
    m = (secs % 3600) / 60;
    s = secs % 60;
}

int main()
{
    int secs;
    int h, m, s;
    cin >> secs;
    whatTime(secs,h,m,s);
    cout << h << ":" << m << ":" << s << endl;
    return 0;
}