#include <iostream>
using namespace std;

class Rectangle
{
    public:
        int height;
        int width;
        void Set(int h, int w);
        int GetArea();
};

void Rectangle::Set(int h, int w)
{
    height = h;
    width = w;
}

int Rectangle::GetArea()
{
    return height * width;
}

Rectangle GetRect(int h, int w)
{
    Rectangle rect;
    rect.Set(h, w);
    return rect;
}

int main()
{
    int h;
    int w;
    int area;
    cin >> h;
    cin >> w;
    Rectangle rect = GetRect(h, w);
    area = rect.GetArea();
    cout << "长方形的面积为：" << area << endl;
    return 0;
}