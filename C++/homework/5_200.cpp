#include <iostream>
#include <cmath>
using namespace std;

class Container {
public:
    virtual double getArea() = 0; // 纯虚函数
    virtual double getVolume() = 0; // 纯虚函数
};

class Sphere : public Container {
    double radius;
public:
    Sphere(double r) : radius(r) {}
    double getArea() {
        return 4 * M_PI * radius * radius;
    }
    double getVolume() {
        return 4.0 / 3.0 * M_PI * pow(radius, 3);
    }
};

class Cylinder : public Container {
    double radius;
    double height;
public:
    Cylinder(double r, double h) : radius(r), height(h) {}
    double getArea() {
        return 2 * M_PI * radius * (radius + height);
    }
    double getVolume() {
        return M_PI * radius * radius * height;
    }
};

class Cube : public Container {
    double side;
public:
    Cube(double s) : side(s) {}
    double getArea() {
        return 6 * pow(side, 2);
    }
    double getVolume() {
        return pow(side, 3);
    }
};

int main(){
    Container *Base = new Sphere(1.0);
    cout << "Sphere Area: " << Base->getArea() << ", Volume: " << Base->getVolume() << endl;
    Base = new Cylinder(1.0, 1.0);
    cout << "Cylinder Area: " << Base->getArea() << ", Volume: " << Base->getVolume() << endl;
    Base = new Cube(1.0);
    cout << "Cube Area: " << Base->getArea() << ", Volume: " << Base->getVolume() << endl;
    return 0;
}