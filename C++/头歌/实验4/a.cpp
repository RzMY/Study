#include <iostream>
using namespace std;

class Chinese
{
    public:
        virtual void greet();
};

void Chinese::greet()
{
    cout << "你好" << endl;
}

class EnglishLearner : public Chinese
{
    public:
        void greet();
};

void EnglishLearner::greet()
{
    cout << "Hello" << endl;
}

class Repeater : public Chinese
{
    public:
        void greet();
};

void Repeater::greet()
{
    Chinese::greet();
}