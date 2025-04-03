#include <iostream>

using namespace std;

// 基类 Shape
class Shape {
   public:
      // 设置宽度
      void setWidth(int w) {
         width = w;
      }
      // 设置高度
      void setHeight(int h) {
         height = h;
      }
   protected:
      int width;
      int height;
};

// 添加空行以分隔类的定义

// 派生类 Rectangle
class Rectangle: public Shape {
   public:
      // 获取面积
      int getArea() { 
         return (width * height); 
      }
};

// 添加空行以分隔类的定义和主函数

int main(void) {
   Rectangle Rect;

   Rect.setWidth(5);
   Rect.setHeight(7);

   // 输出对象的面积
   cout << "Total area: " << Rect.getArea() << endl;

   return 0;
}