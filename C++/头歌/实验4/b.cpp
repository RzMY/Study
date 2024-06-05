#include <iostream>
using namespace std;
 
class Shape
{
    public:
    virtual  void PrintArea()=0;
};
 
class Rectangle : public Shape
{
    public:
        float width;
        float height;
        void PrintArea();
        Rectangle(float w,float h);
    
};

Rectangle::Rectangle(float w,float h)
{
    width=w;
    height=h;
}

void Rectangle::PrintArea()
{
    cout<<"矩形面积 = "<< width*height<<endl;
}
 
 
 
class Circle : public Shape
{
    public:
        float radio;
        void PrintArea();
        Circle(float r);
    
    
};

Circle::Circle(float r)
{
    radio=r;
}

void Circle::PrintArea()
{
    cout<<"圆形面积 = "<<radio * radio * 3.14<<endl;
}