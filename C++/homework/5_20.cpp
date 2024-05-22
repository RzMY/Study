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
    double getArea() override {
        return 4 * M_PI * radius * radius;
    }
    double getVolume() override {
        return 4.0 / 3.0 * M_PI * pow(radius, 3);
    }
};

class Cylinder : public Container {
    double radius;
    double height;
public:
    Cylinder(double r, double h) : radius(r), height(h) {}
    double getArea() override {
        return 2 * M_PI * radius * (radius + height);
    }
    double getVolume() override {
        return M_PI * radius * radius * height;
    }
};

class Cube : public Container {
    double side;
public:
    Cube(double s) : side(s) {}
    double getArea() override {
        return 6 * pow(side, 2);
    }
    double getVolume() override {
        return pow(side, 3);
    }
};

int main(){
    Sphere s(1);
    Cylinder c(1, 1);
    Cube cu(1);
    cout << "Sphere: Area = " << s.getArea() << ", Volume = " << s.getVolume() << endl;
    cout << "Cylinder: Area = " << c.getArea() << ", Volume = " << c.getVolume() << endl;
    cout << "Cube: Area = " << cu.getArea() << ", Volume = " << cu.getVolume() << endl;
    return 0;
}