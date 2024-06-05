#include<iostream>
using namespace std;
class Virus
{
public:
    int Gen=0;
    Virus();
    Virus(Virus& v);
};
 
Virus::Virus()
{
    Gen = 0;
}
Virus::Virus(Virus& v)
{
    this->Gen=v.Gen+1;
}
bool operator==(const int& g, const Virus& v)
{
    if (g == v.Gen)
    {
        return true;
    }
    else
    {
        return false;
    }
    
}
int main()
{
    Virus vs[10];
 
    int pairs[] = { 3,3,2,9,0,8,2,6,6,9,1,1,3,5,8,3,0,6,9,2 };
 
 
    for (int s = 0; s < 20; s += 2)
    {
        Virus v = vs[pairs[s]];
        vs[pairs[s + 1]] = v;
    }
 
    for (int g = 0; g < 5; g++)
    {
        int count = 0;
        for (int i = 0; i < 10; i++)
        {
            if (g == vs[i])
                count++;
        }
        cout << "年龄：" << g << " 数量：" << count << endl;
    }
}