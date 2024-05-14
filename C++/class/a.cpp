#include <iostream>
using namespace std;

class MyVector {
public:
    int v[4];
    MyVector(int a, int b, int c, int d);
    int &operator[](int i) { return v[i]; }
};

MyVector::MyVector(int a, int b, int c, int d) {
    v[0] = a;
    v[1] = b;
    v[2] = c;
    v[3] = d;
}

int main() {
    MyVector v(1, 2, 3, 4);
    cout << v[0] << " " << v[1] << " " << v[2] << " " << v[3] << endl;
    v[0] = 10;
    v[1] = 20;
    v[2] = 30;
    v[3] = 40;
    cout << v[0] << " " << v[1] << " " << v[2] << " " << v[3] << endl;
    return 0;
}