#include <iostream>
using namespace std;

class complex
{
    public:
        double real;
        double imag;
        complex(){}
        complex(int r, int i){
            real = r;
            imag = i;
        }
        complex(int i){real = imag = i/2;}
        operator int(){return real+imag;}
        void print(){
            cout << real << "+" << imag << "i" << endl;
        }
};

int main()
{
    complex a1(1,2);
    complex a2(3,4);
    complex a3;
    a3 = a1 + a2;
    a3.print();
}