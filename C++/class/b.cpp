#include <iostream>
using namespace std;

class AB
{
    public:
        double m;
        AB();
        AB(double i);
        AB(char *s);
        void print();
        operator int() { return m; }// 类型转换函数,将AB转换为int
};

AB::AB()
{
    m = 0;
    cout << "AB()" << endl;
}

AB::AB(double i)
{
    m = i;
    cout << "AB(double)" << endl;
}

AB::AB(char *s)
{
    m = strlen(s);
    cout << "AB(char *)" << endl;
}

void AB::print()
{
    cout << "m = " << m << endl;
}

int main()
{
    AB a;
    a = 10;// 10 is converted to AB(10)
    a.print();
    a = "hello";
    a.print();
    AB a1(123);
    int b1 = a1;
    cout << b1 << endl;
    return 0;
}