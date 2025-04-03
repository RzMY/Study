#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    cout.width(10);
    cout<<123<<endl;
    cout<<123<<endl;
    cout.fill('&');
    cout.width(10);
    cout<<123<<endl;
    cout.precision(4);
    cout<<123.45678<<endl;
    cout << std::fixed;
    cout << 123.45678 << endl;
}