#include <iostream>
using namespace std;

class Test {
    private:
        int val;
    public:
        Test(){
            cout << "default." << endl;
        }
        Test(int n){
            val = n;
            cout << "Con." << endl;
        }
        Test(const Test &t){
            val = t.val;
            cout << "Copy con." << endl;
        }
};

int main(){
    Test t1(6);
    Test t2 = t1;
    Test t3;
    t3 = t1;
    return 0;
}